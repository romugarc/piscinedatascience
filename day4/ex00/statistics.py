def calc_mean(args: tuple) -> None:
    """calc_mean function"""
    if len(args) > 0:
        print("mean:", sum(args) / len(args))
    else:
        print("ERROR")
    return


def calc_median(args: tuple) -> None:
    """calc_median function"""
    if len(args) <= 0:
        print("ERROR")
        return
    largs = list(args)
    largs.sort()
    lena = len(largs)
    if lena % 2 == 0:
        print("median:", largs[lena // 2] + largs[(lena + 1) // 2] / 2)
    else:
        print("median:", largs[lena // 2])
    return


def calc_quartile(args: tuple) -> None:
    """calc_quartile function"""
    if len(args) <= 0:
        print("ERROR")
        return
    largs = list(args)
    largs.sort()
    lena = len(args)
    q_one = lena // 4
    q_three = 3 * lena // 4
    print("quartile:", [float(largs[q_one]), float(largs[q_three])])
    return


def calc_std(args: tuple) -> None:
    """calc_std function"""
    if len(args) <= 0:
        print("ERROR")
        return
    largs = list(args)
    largs.sort()
    mean = sum(args) / len(args)
    difflist = [(item - mean) ** 2 for item in largs]
    var = sum(difflist) / len(largs)
    std = var ** 0.5
    print("std:", std)
    return


def calc_var(args: tuple) -> None:
    """calc_var function"""
    if len(args) <= 0:
        print("ERROR")
        return
    largs = list(args)
    largs.sort()
    mean = sum(args) / len(args)
    difflist = [(item - mean) ** 2 for item in largs]
    var = sum(difflist) / len(largs)
    print("var:", var)
    return


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    This function takes in *args, a quantity of unknown number,
    and make the Mean, Median, Quartile (25% and 75%),
    Standard Deviation and Variance according
    to the **kwargs ask
    """
    try:
        if args is None or kwargs is None:
            raise ValueError("none args/kwargs")
        if any(item is None for item in args):
            raise ValueError("none item args")
        if any(item is None for item in kwargs.items()):
            raise ValueError("none item kwargs")
        if any(item is None for item in kwargs.keys()):
            raise ValueError("none item keys")
        if not all(isinstance(item, (int, float)) for item in args):
            raise ValueError("not int/float in args")
        if not all(isinstance(item, str) for item in kwargs.values()):
            raise ValueError("not str in keys")
        if any(item == "mean" for item in kwargs.values()):
            calc_mean(args)
        if any(item == "median" for item in kwargs.values()):
            calc_median(args)
        if any(item == "quartile" for item in kwargs.values()):
            calc_quartile(args)
        if any(item == "std" for item in kwargs.values()):
            calc_std(args)
        if any(item == "var" for item in kwargs.values()):
            calc_var(args)
    except Exception as e:
        print(f"ERROR:{str(e)}")
        return
