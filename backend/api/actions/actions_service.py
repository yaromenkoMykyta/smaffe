"""
This module provides the implementation of the actions service.

It includes functions for:
- Making an espresso
- Making a cream caffe

Each function delegates the business logic to the
corresponding methods in the `caffe_controller` module.
"""

import backend.core.board.caffee_controller as caffe_controller


def make_espresso():
    """
    Handle the business logic for making an espresso.

    This function delegates the task of making an espresso to the
    `make_espresso` function in the `caffe_controller` module.

    :returns: None
    """
    caffe_controller.make_espresso()


def make_cream_caffe():
    """
    Handle the business logic for making a cream caffe.

    This function delegates the task of making a cream caffe to the
    `make_cream_caffe` function in the `caffe_controller` module.

    :returns: None
    """
    caffe_controller.make_cream_caffe()
