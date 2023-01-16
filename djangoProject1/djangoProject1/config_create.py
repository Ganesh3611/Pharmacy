from configparser import ConfigParser

config = ConfigParser()
config['db'] = {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'db.oracle',
        'USER': 'pharmacy',
        'PASSWORD': 'pharmacy',
        'HOST': 'localhost',
        'PORT': '1521',
        'SID': 'xe'
}

with open('./config.ini','w') as f:
    config.write(f)


