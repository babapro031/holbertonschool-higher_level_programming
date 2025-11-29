#!/usr/bin/python3
"""BaseGeometry class module."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise an exception for unimplemented area method."""
        raise Exception("area() is not implemented")
