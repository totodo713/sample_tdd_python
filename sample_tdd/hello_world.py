#!/usr/bin/python
# -*- coding: utf-8 -*-
"""hello_world module.

Hello world.
This is Testing sample target.

* Author: YAMAGAMI Satoshi
"""


class HelloWorld(object):
    """Hello world.

    Properties:
        * message : str
    """

    @property
    def message(self) -> str:
        """Message.

        Property "message" is said by say().

        :return Current Message.
        """
        return self.__message

    @message.setter
    def message(self, message: str):
        """Set Message.

        :param message : New Message.
        """
        self.__message = message

    def __init__(self, message: str = None):
        """Initialize the class instance.

        Initialize the class.
        And set message if argument is not None.

        :param message : Message.
        """
        self.message = message

    def say(self):
        """Print "message"."""
        print(self.__message)
