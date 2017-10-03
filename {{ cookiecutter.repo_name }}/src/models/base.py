# -*- coding: utf-8 -*-
"""
base.py

    Base model class

@author: Douglas Daly
@date: 9/30/2017
"""
#
#   Imports
#
from abc import ABCMeta, abstractmethod


#
#   Class Definitions
#

class Model(object, metaclass=ABCMeta):
    """
    Base Model Class
    """

    def __init__(self):
        """ Default Constructor
        """
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

        :return: Parameters dictionary
        :rtype: dict

        """
        return self._parameters

    @parameters.setter
    def parameters(self, params):
        """ Sets the parameters for this model

        :param dict params: Full parameters dictionary to use

        """
        self._parameters = params

    def add_parameter(self, param, value):
        """ Adds a single parameter to the parameter set

        :param str param: Parameter to add
        :param value: Value for the given parameter

        """
        raise NotImplementedError()

    def remove_parameter(self, param):
        """ Removes the specified parameter from the model parameters

        :param str param: Name of the parameter to remove

        :return: Value of the parameter removed, None if param not in set

        """
        if param in self.parameters.keys():
            ret = self._parameters.pop(param)
        else:
            ret = None

        return ret

    def _check_parameter(self, param, value):
        """ Checks if the given parameter and value combination are valid for this model

        :param str param: Parameter name
        :param value: Parameter value

        :return: If the given parameter and value combination are valid for this model
        :rtype: bool

        """
        raise NotImplementedError()

    @property
    def hyper_parameters(self):
        """ Hyper-parameters which are currently set for this model

        :return: Hyper-parameters dictionary
        :rtype: dict

        """
        return self._hyper_parameters

    @hyper_parameters.setter
    def hyper_parameters(self, hyper_params):
        """ Sets the hyper-parameters for this model

        :param hyper_params:

        """
        self._hyper_parameters = hyper_params

    def add_hyper_parameter(self, hyper_param, value):
        """ Adds a single hyper-parameter to the hyper-parameter set

        :param str hyper_param: Hyper-parameter to add
        :param value: Value for the given hyper-parameter

        """
        raise NotImplementedError()

    def remove_hyper_parameter(self, hyper_param):
        """ Removes the specified hyper-parameter from the model hyper-parameters

        :param str hyper_param: Name of the hyper-parameter to remove

        :return: Value of the hyper-parameter removed, None if hyper_param not in set

        """
        if hyper_param in self.hyper_parameters.keys():
            ret = self._hyper_parameters.pop(hyper_param)
        else:
            ret = None

        return ret

    def _check_hyper_parameter(self, hyper_param, value):
        """ Checks if the given hyper-parameter and value combination are valid for this model

        :param str hyper_param: Hyper-Parameter name
        :param value: Hyper-Parameter value

        :return: If the given hyper-parameter and value combination are valid for this model
        :rtype: bool

        """
        raise NotImplementedError()

    @property
    def results(self):
        """ Result metrics from the training process

        :return: Results dictionary
        :rtype: dict

        """
        return self._results

    # Abstract Methods

    @abstractmethod
    def construct(self, **kwargs):
        """ Constructs the model from the set parameters

        :param kwargs: Additional options for construction

        :return: Result of model construction
        :rtype: bool

        """
        pass

    @abstractmethod
    def run(self):
        """ Runs the primary preset training routine

        :return: Result of training run (success or failure)
        :rtype: bool

        """
        pass

    @abstractmethod
    def train(self, X, y, **kwargs):
        """ Trains the model on the given X and y Data

        :param X: Training data features
        :param y: Training data values/labels
        :param kwargs: Additional options for training

        :return: Result of the training operation (success or failure)
        :rtype: bool

        """
        pass

    @abstractmethod
    def predict(self, X, **kwargs):
        """ Uses the trained model to predict outputs for the given features

        :param X: Features to predict outputs for
        :param kwargs: Additional options for prediction

        :return: Prediction y data on given X data
        :rtype: numpy.ndarray

        """
        pass

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
