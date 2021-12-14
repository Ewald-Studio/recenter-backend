SECRET_KEY = 'django-insecure-...'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recenter',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',    
    }
}

MEDIA_ROOT = '/home/arch1/projects/recenter/app/media'



