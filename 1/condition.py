def get_function():
    return lambda x1, x2: (x1 + x2 - 1)**2 + x1**2 - 2 * x2


def get_function_as_string():
    return "(x1 + x2 - 1)**2 + x1**2 - 2 * x2"


def get_gradient():
    return lambda x1, x2: (4 * x1 + 2 * x2 - 2, 2 * x1 + 2 * x2 - 4)


def get_hessian():
    return lambda: ((4, 2),
                    (2, 2))
