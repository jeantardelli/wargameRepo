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
