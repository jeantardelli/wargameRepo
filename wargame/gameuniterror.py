"""wargame.gameuniterror

Shows how to create a custom exception class for the Attack of the Orcs game.

This modue is compatible with Python 3.5.x and later. It contains supporting
code for the book, Learning Python Application Development Packt Publishing.

This is my version of the code, it is pretty much similar to the original
author's version.

RUNNING THE PROGRAM:
--------------------
This is NOT run as a standalone program. See `wargame/attackoftheorcs.py`

# ----------------------------------------------------------------------------
# Alternate implementation where you subclass the custom exception,
# GameUnitError. The following code would eliminate the need of maintaining
# an error_dict object in GameUnitError.
# ----------------------------------------------------------------------------
# class GameUnitError(Exception):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.padding = '~'*50 + '\n'
#         self.error_message = " Unspecified Error!"
#
# class HealthMeterException(GameUnitError):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.error_message = (self.padding +
#                              "ERROR: Health Meter Problem" +
#                              '\n' + self.padding )
#
# class AttackException(GameUnitError):
#     # Code similar to that of HealthMeterException .
#     pass

.. seealso:: `wargame/attackoftheorcs.py`

:copyright: 2020, Jean Tardelli
:license: The MIT License (MIT). See LICENSE file for further details.
"""

class GameUnitError(Exception):
    """Custom exceptions class for the `AbstractGameUnit` and its subclasses

    Inherits built-in `Exception` class.

    :ivar error_message: Print the error message with an error code.
    :ivar error_dict: Python dictionary object that stores error number as
                      the key and the detailed error message as its value.

    .. seealso:: :py:meth: `abstractgameunit.AbstractGameUnit.heal` for an
                 example usage.
    """
    def __init__(self, message='', code=000):
        super().__init__(message)
        self.error_message = '~'*50 + '\n'

        # Alternative approach is to subclass GameUnitError
        self.error_dict = {
            000: "ERROR-000: Unspecified Error!",
            101: "ERROR-101: Health Meter Problem!",
            102: "ERROR-102: Attack issue! Ignored",
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~'*50
