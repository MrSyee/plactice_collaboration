"""Simple calculator example for the practice of collaboration."""


class Calculator(object):
    """Simple calculator which has 4 functionalities.

    => add, sub, mul, div
    => bitwise_shift_left, bitwise_shift_right, bitwise_and
    => bitwise_or, bitwise_not, bitwise_xor

    All methods will be implemented as staticmethods
    so that it can be called without making an object.

    !!Don't forget to run static analyzers and unittests
    before pushing your code. (check 100% test covered)
    """

    def add(self, x: float, y: float) -> float:
        """Return the sum of two inputs.

        Given two numbers of float type x, y
        returns float type x + y

        Arg:
            x (float) : The first element of sum.
            y (float) : The second element of sum.

        Return:
            float : The sum of two given numbers.
        """
        return x + y

    def minus(self, x: float, y: float) -> float:
        """Return the minus of two inputs."
        pass
