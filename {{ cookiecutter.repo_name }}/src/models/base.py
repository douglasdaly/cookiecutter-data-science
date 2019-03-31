# -*- coding: utf-8 -*-
"""
Base classes for the Parameterize Model package.
"""
#
#   Imports
#
import os
import pickle
from abc import ABCMeta, abstractmethod

from .parameters.base import Parameter
from .parameters.base import ParameterStore


#
#   Class Definitions
#

class Model(object, metaclass=ABCMeta):
    """
    Model class
    """
    _parameter_store_cls = ParameterStore
    _default_parameter_cls = Parameter
    _default_hyper_parameter_cls = Parameter

    def __init__(self):
        self._parameters = self._parameter_store_cls()
        self._hyper_parameters = self._parameter_store_cls()

        self._results = None

    # dunder methods

    # Properties

    @property
    def parameters(self):
        """ParameterStore: Parameters which are currently set."""
        return self._parameters

    @property
    def hyper_parameters(self):
        """ParameterStore: Hyper-parameters which are currently set."""
        return self._hyper_parameters

    @property
    def results(self):
        """dict: Fitting result metrics."""
        return self._results

    # Parameter functions

    def add_parameter(self, *args, **kwargs):
        """Adds a hyper-parameter to the model

        Adds a :class:`Parameter` instance (using the given `args`
        and `kwargs` in the constructor if the first `arg` is not a
        :class:`Parameter` instance) to this model's hyper-parameters.

        Parameters
        ----------
        args
            Either the instantiated :class:`Parameter` class or the
            arguments to pass to the default parameter class's constructor.
        kwargs : optional
            Keyword arguments to pass to the default Parameter class's
            constructor.

        """
        if args and isinstance(args[0], Parameter):
            self._parameters.add(args[0])
        else:
            self._parameters.add(
                self._default_parameter_cls(*args, **kwargs)
            )
        return

    def remove_parameter(self, name):
        """Removes a parameter from the model

        Parameters
        ----------
        name : str
            The name of the parameter to remove.

        Returns
        -------
        Parameter
            The removed parameter object.

        Raises
        ------
        MissingParameterException
            If the specified `name` is not a hyper-parameter.

        """
        return self._hyper_parameters.remove(name)

    def set_parameter(self, name: str, value) -> None:
        """Sets a parameter value

        Will add the given `param` and `value` to the parameters if
        they are valid, throws an exception if they are not.

        Parameters
        ----------
        name : str
            Parameter to set the value for.
        value
            Value to set.

        Raises
        ------
        InvalidParameterException
            If the given `name` or `value` are not valid.

        See Also
        --------
        parameters, remove_parameter

        """
        self._parameters[name] = value
        return

    def unset_parameter(self, name: str) -> object:
        """Unsets a parameter value

        Removes the specified parameter's value from the parameter values
        if it is part of the parameter set and returns its current value.

        Parameters
        ----------
        name : str
            Name of the parameter whose value needs to be un-set.

        Returns
        -------
        object
            Previously set value of the parameter.

        Raises
        ------
        MissingParameterException
            If the parameter to remove does not exist in the set of parameters.

        See Also
        --------
        parameters, add_parameter

        """
        return self._parameters.pop(name)

    # - Hyper-parameters

    def add_hyper_parameter(self, *args, **kwargs):
        """Adds a hyper-parameter to the model

        Adds a :class:`Parameter` instance (using the given `args`
        and `kwargs` in the constructor if the first `arg` is not a
        :class:`Parameter` instance) to this model's hyper-parameters.

        Parameters
        ----------
        args
            Either the instantiated :class:`Parameter` class or the
            arguments to pass to the default parameter class's constructor.
        kwargs : optional
            Keyword arguments to pass to the default Parameter class's
            constructor.

        """
        if args and isinstance(args[0], Parameter):
            self._hyper_parameters.add(args[0])
        else:
            self._hyper_parameters.add(
                self._default_hyper_parameter_cls(*args, **kwargs)
            )
        return

    def remove_hyper_parameter(self, name):
        """Removes a hyper-parameter from the model

        Parameters
        ----------
        name : str
            The name of the hyper-parameter to remove.

        Returns
        -------
        Parameter
            The removed parameter object.

        Raises
        ------
        MissingParameterException
            If the specified `name` is not a hyper-parameter.

        """
        return self._hyper_parameters.remove(name)

    def set_hyper_parameter(self, name, value):
        """Sets a hyper-parameter value

        Sets a hyper-parameter's value if the given `hyper_param` and `value`
        are valid.

        Parameters
        ----------
        name : str
            Hyper-parameter to set value for.
        value
            Value to set.

        Raises
        ------
        MissingParameterException
            If the given `name` hyper-parameter does not exist.
        InvalidParameterException
            If the given `value` is not valid for the specified
            hyper-parameter.

        See Also
        --------
        hyper_parameters, remove_hyper_parameter

        """
        self._hyper_parameters[name] = value
        return

    def unset_hyper_parameter(self, name):
        """Un-sets a hyper-parameter

        Un-sets the specified hyper-parameter's value from the set of
        hyper-parameters and returns the previously set value.

        Parameters
        ----------
        name : str
            Name of the hyper-parameter to clear the value for.

        Returns
        -------
        object
            Previously set value of the hyper-parameter.

        Raises
        ------
        MissingParameterException
            If the given `name` hyper-parameter does not exist.

        See Also
        --------
        hyper_parameters, add_hyper_parameter

        """
        return self._hyper_parameters.pop(name)

    # Save/Load methods

    @classmethod
    def _get_model_directory(cls, tag, project_dir=None):
        """Gets the storage Directory

        Returns the directory where this models `parameters`,
        `hyper_parameters` as well as any other data required for the model
        is stored under a unique `tag` name.

        Parameters
        ----------
        tag: str
            Tag to use for the directory.
        project_dir : str, optional
            Base project directory path.

        Returns
        -------
        str
            Path to the default model storage directory.

        """
        ret = os.path.join('models/%s' % cls.__name__.lower(), tag)
        if project_dir:
            ret = os.path.join(project_dir, ret)
        return ret

    def save(self, tag, overwrite_existing=False, project_dir=None):
        """Saves this model

        Saves this model's `parameters`, `hyper_parameters` as well as
        any other data required to reconstruct this model.  Saves this
        data with the given unique `tag` name.

        Parameters
        ----------
        tag : str
            Tag to use to save the model data.
        overwrite_existing : bool, optional
            Whether to overwrite any existing saved model with the same
            `tag` (Default is False).
        project_dir : str, optional
            Base project directory path.

        Returns
        -------
        bool
            Success or failure of the save.

        """
        model_dir = self._get_model_directory(tag, project_dir=project_dir)
        if not model_dir:
            os.mkdir(model_dir)

        parameters_file = os.path.join(model_dir, "parameters.pkl")
        if os.path.exists(parameters_file) and not overwrite_existing:
            return False
        with open(parameters_file, 'wb') as fout:
            pickle.dump(self._parameters, fout)

        hyper_parameters_file = os.path.join(model_dir, "hyper_parameters.pkl")
        if os.path.exists(hyper_parameters_file) and not overwrite_existing:
            return False
        with open(hyper_parameters_file, 'wb') as fout:
            pickle.dump(self._hyper_parameters, fout)

        return True

    @classmethod
    def load(cls, tag, project_dir=None):
        """Loads a saved model instance

        Loads saved model `parameters` and `hyper_parameters` as well
        as any serialized model-specific objects from a saved version
        with the `tag` specified (from the base `project_dir`).

        Parameters
        ----------
        tag : str
            Tag to use to load the model data.
        project_dir : str, optional
            Base project directory path.

        Returns
        -------
        Model
            Model loaded from disk.

        """
        model_dir = cls._get_model_directory(tag, project_dir=project_dir)
        if not model_dir:
            return False

        instance = cls()

        parameters_file = os.path.join(model_dir, "parameters.pkl")
        with open(parameters_file, 'rb') as fin:
            instance._parameters = pickle.load(fin)

        hyper_parameters_file = os.path.join(model_dir, "hyper_parameters.pkl")
        with open(hyper_parameters_file, 'rb') as fin:
            instance._hyper_parameters = pickle.load(fin)

        return instance

    # Abstract methods

    def construct(self, *args, **kwargs):
        """Constructs the model

        Constructs the model based on the set `parameters` (if needed).

        Parameters
        ----------
        args : optional
            Any additional arguments to use in construction call.
        kwargs : optional
            Any additional keyword arguments to use in construction call.

        Returns
        -------
        bool
            Result of model construction (success or failure).

        """
        return

    @abstractmethod
    def fit(self, x, y, *args, **kwargs):
        """Fits the model

        Fits the constructed model using the parameters and hyper-parameters
        specified.

        Parameters
        ----------
        x
            X-data to use in fitting the model.
        y
            Y-data to use in fitting the model.
        args : optional
            Any additional arguments to use in fit call.
        kwargs : optional
            Any additional keyword arguments to use in fit call.

        Returns
        -------
        bool
            Result of the training operation (success or failure).

        """
        pass

    @abstractmethod
    def predict(self, x, *args, **kwargs):
        """Predict outputs

        For the given input(s), run the trained model to generate
        outputs.

        Parameters
        ----------
        x
            Inputs to predict outputs for.
        args : optional
            Additional parameter to pass to prediction call.
        kwargs : optional
            Additional keyword arguments to pass to prediction call.

        Returns
        -------
        object
            Predictions from the given `x` data.

        """
        pass


#
#   Exceptions
#

class ModelException(Exception):
    """
    Base class for Model exceptions.
    """
    pass
