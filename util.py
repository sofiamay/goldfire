def str_to_int(string):
    try:
        return int(string)
    except ValueError:
        raise ValueError("You must input an integer")
