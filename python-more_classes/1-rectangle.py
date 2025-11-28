#!/usr/bin/python3
"""This module defines a Rectangle class with width and height attributes.

The class includes getter and setter methods for width and height with
validation to ensure they are integers greater than or equal to 0.
"""


class Rectangle:
    """Rectangle class with private width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance 
        with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
