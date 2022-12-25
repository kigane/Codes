def partial(func, *part_args):
    def wrapper(*extra_args):
        args = list(part_args)
        args.extend(extra_args)
        return func(*args)

    return wrapper