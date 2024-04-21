class InvalidInputException(Exception):
    pass


class OccupiedTableException(Exception):
    pass


class TooSmallTableException(Exception):
    pass


class EmptyTableException(Exception):
    pass


class AccessDeniedException(Exception):
    def __init__(self, error_string):
        self.error_string = error_string

    def __str__(self):
        return f'ERROR: {self.error_string}'
