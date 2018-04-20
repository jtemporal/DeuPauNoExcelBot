from decouple import config

HOSTNAME = 'localhost'

SECRET_KEY = ''

PLATFORMS = {
    'telegram': {
        'ENGINE': 'bottery.platform.telegram',
        'OPTIONS': {
            'token': config('TELEGRAM_TOKEN')
        }
    },
}
