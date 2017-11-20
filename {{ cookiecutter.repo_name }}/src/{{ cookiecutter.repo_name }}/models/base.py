# -*- coding: utf-8 -*-
"""
Implements the Model abstract class which is extended for specific
model implementations.

Also implements the ModelException, InvalidParameterException and
InvalidHyperParameterException exceptions.

"""
#
#   Imports
#
import os
from abc import ABCMeta, abstractmethod

from ..data import save_data_to_pickle, load_data_from_pickle


#
#   Class Definitions
#

class Model(object, metaclass=ABCMeta):
    """
    Base Model Class

    Attributes
    ----------
    parameters : dict
        Dictionary of parameters for this model with their associated
        values.
    hyper_parameters: dict
        Dictionary of hyper-parameters for training this model with
        their associated values.
    results: dict
        Dictionary of training results and their associated values.

    """

    def __init__(self):
        self._parameters = dict()
        self._hyper_parameters = dict()

        self._results = None

        self._opts_parameters = None
        self._opts_hyper_parameters = None
        self._opts_results = None

    # Properties

    @property
    def parameters(self):
        """ Parameters which are currently set for this model
        """
        return self._parameters

    @parameters.setter
    def parameters(self, params):
        """ Sets the parameters

        Sets the parameters to the given `params` dictionary if they
        are all valid parameters.

        Parameters
        ----------
        params: dict
            Full parameters dictionary to use

        Raises
        ------
        InvalidParameterException
            If one of the given parameters and/or value given is not
            valid.

        See Also
        --------
        parameters, add_parameter, remove_parameter

        """
        self._parameters.clear()
        for k, v in params.items():
            self.add_parameter(k, v)

    def add_parameter(self, param, value):
        """ Adds a parameter

        Will add the given `param` and `value` to the parameters if
        they are valid, throws an exception if they are not.

        Parameters
        ----------
        param: str
            Parameter to add
        value:
            Value for the given parameter

        Raises
        ------
        InvalidParameterException
            If the given `param` and/or `value` are not valid

        See Also
        --------
        parameters, remove_parameter

        """
        if self._check_parameter(param, value):
            self._parameters[param] = value

    def remove_parameter(self, param):
        """ Removes a parameter

        Removes the specified `param` from the parameters set if it is
        part of the parameter set and returns its currently set value,
        returns None if it's not a parameter.

        Parameters
        ----------
        param: str
            Name of the parameter to remove

        Returns
        -------
        object or None
            Value of the parameter removed, None if param not in set

        See Also
        --------
        parameters, add_parameter

        """
        if param in self.parameters.keys():
            ret = self._parameters.pop(param)
        else:
            ret = None

        return ret

    def _check_parameter(self, param, value, suppress_exceptions=False):
        """ Checks the given parameter and value combination

        Checks the `param` and `value` given to see if  they are valid
        against the set of parameter options specified in the class's
        definition.

        Parameters
        ----------
        param: str
            Parameter name
        value:
            Parameter value

        suppress_exceptions: bool, optional
            Whether or not to ignore exceptions (Default is False)

        Returns
        -------
        bool
            If the given parameter and value combination are valid
        str
            Error string if they're not valid, otherwise None

        Raises
        ------
        InvalidParameterException
            If `suppress_exceptions` is False and the given `param` and
            `value` combination are not valid.

        See Also
        --------
        __param_check_helper

        """
        except_type = None if suppress_exceptions \
            else InvalidParameterException
        return self.__param_check_helper(param, value, self._opts_parameters,
                                         except_type)

    @property
    def hyper_parameters(self):
        """ Hyper-parameters which are currently set for this model
        """
        return self._hyper_parameters

    @hyper_parameters.setter
    def hyper_parameters(self, hyper_params):
        """ Sets the hyper-parameters

        Sets the hyper-parameters to the given `hyper_params`
        dictionary if they are all valid hyper-parameters.

        Parameters
        ----------
        hyper_params: dict
            Hyper-parameter dictionary to set for this model

        Raises
        ------
        InvalidHyperParameterException
            If one of the given hyper-parameters and/or values is not
            valid.

        See Also
        --------
        hyper_parameters, add_hyper_parameter, remove_hyper_parameter

        """
        self._hyper_parameters.clear()
        for k, v in hyper_params.items():
            self.add_hyper_parameter(k, v)

    def add_hyper_parameter(self, hyper_param, value):
        """ Adds a hyper-parameter

        Adds a single hyper-parameter to the set of hyper-parameters if
        the given `hyper_param` and `value` are valid.

        Parameters
        ----------
        hyper_param: str
            Hyper-parameter to add
        value:
            Value for the given hyper-parameter

        Raises
        ------
        InvalidHyperParameterException
            If the given `hyper_param` and/or `value` is not valid

        See Also
        --------
        hyper_parameters, remove_hyper_parameter

        """
        if self._check_hyper_parameter(hyper_param, value):
            self._hyper_parameters[hyper_param] = value

    def remove_hyper_parameter(self, hyper_param):
        """ Removes a hyper-parameter

        Removes the specified `hyper_param` from the set of
        hyper-parameters if it's set and returns the current value, if
        it's not set it returns None.

        Parameters
        ----------
        hyper_param: str
            Name of the hyper-parameter to remove

        Returns
        -------
        object or None
            Value of the hyper-parameter removed, None if `hyper_param`
            not in set

        See Also
        --------
        hyper_parameters, add_hyper_parameter

        """
        if hyper_param in self.hyper_parameters.keys():
            ret = self._hyper_parameters.pop(hyper_param)
        else:
            ret = None

        return ret

    def _check_hyper_parameter(self, hyper_param, value,
                               suppress_exceptions=False):
        """ Checks a hyper-parameter

        Checks the given `hyper_param` and `value` for validity against
        the opts_hyper_parameters

        Parameters
        ----------
        hyper_param: str
            Hyper-Parameter name
        value:
            Hyper-Parameter value
        suppress_exceptions: bool, optional
            Whether or not to ignore exceptions (Default is to False)

        Returns
        -------
        bool
            If the given `hyper_param` and `value` combination are
            valid
        str
             Error string if not valid, None otherwise

        Raises
        ------
        InvalidHyperParameterException
            If `suppress_exceptions` is False and the given
            `hyper_param` and `value` combination are not valid

        See Also
        --------
        __param_check_helper

        """
        except_type = None if suppress_exceptions \
            else InvalidHyperParameterException
        return self.__param_check_helper(hyper_param, value,
                                         self._opts_hyper_parameters,
                                         except_type)

    @staticmethod
    def __param_check_helper(param, value, option_dict, exception_type=None):
        """ Helper function for checking given Parameter and Value

        Given a `option_dict` - a dictionary of parameters to
        _ParamOption values, checks the validity of the given `param`
        and `value`.

        Parameters
        ----------
        param: str
            Name of the parameter to check
        value: object
            Value for the given parameter
        option_dict: dict of {str: _ParamOption}
            Dictionary of allowed parameter options
        exception_type: ModelException or None, optional
            Type of Exception to throw if the given `param` and `value`
            pair given are not valid

        Returns
        -------
        bool
            Whether or not the given parameter pair are valid
        str
            Error string if the pair given are invalid, None if they
            are valid

        """
        if exception_type is not None:
            suppress_exceptions = False
        else:
            suppress_exceptions = True

        if param not in option_dict.keys():
            err_str = "No parameter named: " + param
            if not suppress_exceptions:
                raise exception_type(err_str)
            return False, err_str

        param_opt = option_dict[param]
        if not isinstance(value, param_opt.value_type):
            err_str = "Invalid type for " + param + ": found " + \
                      str(type(value)) + ", expected: " + \
                      str(param_opt.value_type)
            if not suppress_exceptions:
                raise exception_type(err_str)
            return False, err_str

        if param_opt.value_bounds is not None:
            if param_opt.value_bounds[0] is not None \
                            and value < param_opt.value_bounds[0]:
                err_str = "Invalid value given for " + param + \
                          ": Under min value of " + \
                          str(param_opt.value_bounds[0])
                if not suppress_exceptions:
                    raise exception_type(err_str)
                return False, err_str

            if param_opt.value_bounds[1] is not None \
                    and value > param_opt.value_bounds[1]:
                err_str = "Invalid value given for " + param + \
                          ": Over max value of " + \
                          str(param_opt.value_bounds[1])
                if not suppress_exceptions:
                    raise exception_type(err_str)
                return False, err_str

        return True, None

    def _check_init_parameters(self, use_defaults=True):
        """ Checks/initializes parameters

        Checks whether or not all the required `parameters` are set,
        oiptionally setting them to their default values if they're
        missing and the `use_defaults` flag is set.

        Parameters
        ----------
        use_defaults: bool, optional
            Use default values for required parameters that aren't set

        Returns
        -------
        bool
            Whether or not the parameters in place are sufficient

        """
        additional = self.__check_init_params_helper(self.parameters,
                                                     self._opts_parameters,
                                                     use_defaults)
        if additional is not None:
            for k, v in additional.items():
                self._parameters[k] = v
            return True
        else:
            return False

    def _check_init_hyper_parameters(self, use_defaults=True):
        """ Checks/initializes hyper-parameters

        Checks whether or not all the required `hyper_parameters` are
        set, optionally setting them to their default values if
        they're missing and the `use_defaults` flag is set.

        Parameters
        ----------
        use_defaults: bool, optional
            Use default values for required hyper-parameters that
            aren't set

        Returns
        -------
        bool
            Whether or not the hyper-parameters in place are sufficient

        """
        additional = self.__check_init_params_helper(self.hyper_parameters,
            self._opts_hyper_parameters,
            use_defaults)
        if additional is not None:
            for k, v in additional.items():
                self._hyper_parameters[k] = v
            return True
        else:
            return False

    @staticmethod
    def __check_init_params_helper(params, opt_params, use_defaults=True):
        """ Helper for checking/initializing parameters

        Helper function which takes the given `params` and `opt_params`
        dictionaries and checks the `params`, optionally setting any
        missing required values to their defaults if the `use_defaults`
        flag is set.

        Parameters
        ----------
        params: dict
            Params to check
        opt_params: dict
            Params options dictionary to check against
        use_defaults: bool, optional
            Use default values for required params that are unset
            (Default is True)

        Returns
        -------
        dict or None
            Additional params to add (None on error)

        """
        dict_additional = dict()
        for k, v in opt_params.items():
            if v.value_required:
                if k not in params.keys():
                    if use_defaults and v.value_default is not None:
                        dict_additional[k] = v.value_default
                    else:
                        return None
        return dict_additional

    @property
    def results(self):
        """ Training result metrics
        """
        return self._results

    # Save/Load Methods

    def __get_model_directory(self, tag):
        """ Gets the storage Directory

        Returns the directory where this models `parameters`,
        `hyper_parameters` as well as any other data required for the model
        is stored under a unique `tag` name.

        Parameters
        ----------
        tag: str
            Tag to use for the directory

        Returns
        -------
        str
            Path to the model storage directory

        """
        raise NotImplementedError()

    def save(self, tag, overwrite_existing=False):
        """ Saves this model

        Saves this model's `parameters`, `hyper_parameters` as well as
        any other data required to reconstruct this model.  Saves this
        data with the given unique `tag` name.

        Parameters
        ----------
        tag: str
            Tag to use to save the model data
        overwrite_existing: bool, optional
            Whether to overwrite any existing saved model with the same
            `tag` (Default is False).

        Returns
        -------
        bool
            Success or failure of the save

        """
        model_dir = self.__get_model_directory(tag)
        if not model_dir:
            os.mkdir(model_dir)

        parameters_file = os.path.join(model_dir, "parameters.pkl")
        if os.path.exists(parameters_file) and not overwrite_existing:
            return False
        save_data_to_pickle(self._parameters, parameters_file,
                            overwrite=overwrite_existing)

        hyper_parameters_file = os.path.join(model_dir, "hyper_parameters.pkl")
        if os.path.exists(hyper_parameters_file) and not overwrite_existing:
            return False
        save_data_to_pickle(self._hyper_parameters, hyper_parameters_file,
                            overwrite=overwrite_existing)

        return self._save_model_helper(model_dir)

    def _save_model_helper(self, directory):
        """ Saves model objects

        Helper function to save model-specific data/objects other than
        `parameters` or `hyper_parameters` that are needed  to
        reconstruct the model.

        Parameters
        ----------
        directory: str
            Location to save the model to

        Returns
        -------
        bool
            Success or failure of the save

        """
        return True

    def load(self, tag):
        """ Loads a model

        Loads saved model `parameters` and `hyper_parameters` as well
        as any serialized model-specific objects from a saved version.

        Parameters
        ----------
        tag: str
            Tag to use to load the model data

        Returns
        -------
        bool
            Result of the model load process

        """
        model_dir = self.__get_model_directory(tag)
        if not model_dir:
            return False

        parameters_file = os.path.join(model_dir, "parameters.pkl")
        self._parameters = load_data_from_pickle(parameters_file)

        hyper_parameters_file = os.path.join(model_dir, "hyper_parameters.pkl")
        self._hyper_parameters = load_data_from_pickle(hyper_parameters_file)

        return self._load_model_helper(model_dir)

    def _load_model_helper(self, directory):
        """ Loads model objects

        Helper function to load model-specific data/objects other than
        `parameters` or `hyper_parameters` that are needed to
        reconstruct the model.

        Parameters
        ----------
        directory: str
            Directory to load the model from

        Returns
        -------
        bool
            Success or failure of the load

        """
        return True

    # Abstract Model Methods

    @abstractmethod
    def construct(self, **kwargs):
        """ Constructs the model

        Constructs the model based on the set `parameters`.

        Parameters
        ----------
        kwargs: dict
            Any additional options for construction

        Returns
        -------
        bool
            Result of model construction (success or failure)

        """
        pass

    @abstractmethod
    def fit(self, **kwargs):
        """ Fits the model

        Fits the constructed model using the parameters and hyper-parameters
        specified.

        Parameters
        ----------
        kwargs: dict
            Additional options for training

        Returns
        -------
        bool
            Result of the training operation (success or failure)

        """
        pass

    @abstractmethod
    def predict(self, x, **kwargs):
        """ Predict outputs

        For the given features, run the trained model to generate
        outputs.

        Parameters
        ----------
        x: numpy.ndarray
            Features to predict outputs for
        kwargs: dict
            Additional options for prediction

        Returns
        -------
        numpy.ndarray
            Prediction y data on given `x` data

        """
        pass

    # - Internal Classes

    class _ParameterOption(object):
        """
        Parameter Option internal class

        Parameters
        ----------
        name: str
            Name of the Parameter these options are for.
        value_type: type
            The type of value for this parameter.
        value_required: bool, optional
            Whether or not this is a required parameter (default is True).
        value_bounds: tuple of (min, max), optional
            Bounds for this parameter (default is None), None can be
            used to specify no limit to a min or max.
        value_default: object, optional
            Default value for this parameter (default is None).

        Attributes
        ----------
        name: str
            Name of the Parameter
        value_type: type
            The type of value for this parameter
        value_required: bool
            Whether or not this is a required parameter
        value_bounds: tuple of (min, max) or None
            Bounds for this parameter
        value_default: object
            Default value for this parameter

        """
        def __init__(self, name, value_type, value_required=True,
                     value_bounds=None, value_default=None):
            self.name = name
            self.value_type = value_type
            self.value_required = value_required
            self.value_bounds = value_bounds
            self.value_default = value_default


#
#   Exception Classes
#

class ModelException(Exception):
    """
    Base Class for Model Exceptions
    """
    pass


class InvalidParameterException(ModelException):
    """
    Thrown when an Invalid Parameter is given
    """
    pass


class InvalidHyperParameterException(ModelException):
    """
    Thrown when an Invalid Hyper-Parameter is given
    """
    pass
