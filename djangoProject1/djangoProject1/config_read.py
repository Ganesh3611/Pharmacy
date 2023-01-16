from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

print(parser.get('db', 'engine'))
print('db' in parser)