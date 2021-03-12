def print_args(fixed_arg, *args, **kwargs):
    print(fixed_arg)
    print(args)
    print(kwargs)

print_args('foo', 'bar', 'baz', meditation = 'zazen', minutes = 40)
