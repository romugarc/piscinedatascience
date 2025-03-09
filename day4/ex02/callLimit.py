def callLimit(limit: int):
    """callLimit decorator"""
    count = 0

    def callLimiter(function):
        """callLimiter wrapper"""

        def limit_function(*args: any, **kwds: any):
            """nonlimit function"""
            nonlocal count
            if count < limit:
                count += 1
                return function()
            else:
                print(f"Error:{str(function)} called too many times")
                return None
        return limit_function
    return callLimiter
