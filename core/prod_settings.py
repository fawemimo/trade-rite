from decouple import config
DEBUG=True
ALLOWED_HOSTS =['localhost','trade-rite.ng', 'www.trade-rite.ng','127.0.0.1']



# AWS CONSOLE CONFIG
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME =config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN="%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS={"CacheControl": "max-age=86400"}
AWS_DEFAULT_ACL = 'public-read'

AWS_LOCATION = 'static'

#  AWS 
STATIC_URL = 'https://%s/%s'%(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION) #AWSSTATIC
MEDIA_URL = 'https://%s/%s/'%(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)


DEFAULT_FILE_STORAGE = 'core.storages.MediaStore'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("NAME"),
        'USER': config("USER"),
        'PASSWORD': config("PASSWORD"),
        'HOST': config("HOST"),
        'PORT':config("PORT")
    }
}

