def square(x: int | float) -> int | float:
    """square function"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """pow function"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer function"""
    count = 0

    def inner() -> float:
        """inner function"""
        nonlocal count
        if function is None:
            return count
        if not isinstance(x, (int, float)):
            return count
        if count != 0:
            count = function(count)
        else:
            count = function(x)
        return count
    return inner
