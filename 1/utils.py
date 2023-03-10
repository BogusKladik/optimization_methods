def decimal_places(accuracy):
    decimal_places = len(str(accuracy)) - 1

    return decimal_places


def count_data(accuracy):
    n = 10**decimal_places(accuracy)

    return n
