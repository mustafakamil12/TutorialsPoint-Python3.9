def print_kwargs(**kwargs):
  for name, value in kwargs.items():
    print('{0} = {1}'.format(name, value))

print_kwargs(meditation = 'zazen', minutes = 40)
