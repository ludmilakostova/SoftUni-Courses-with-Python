class MustContainAtSymbolError(Exception):
    """Raises if @ not present in the e-mail"""
    pass


class NameTooShortError(Exception):
    """Raised if username too small"""
    pass


class InvalidDomainError(Exception):
    """Raised when domain is invalid - out of allowed domains mentioned below"""
    pass


class TooManySymbolsAt(Exception):
    """Raised if more than @ are inputted"""
    pass
