from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

print(list(config.sections()))
print(list(config['account']))

print(config['account']['pin'])
config.set('account','pin','5555')

config.add_section('bank')
config.set('bank','name','hsbc')

with open('config.ini','w') as configfile:
    config.write(configfile)