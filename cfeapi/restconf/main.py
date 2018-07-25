#defautl permission and Default authentication classes
#Setting the authentication default scheme. see docs online @ www.django-rest-framework.org/api-guide/authentication

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication', # Can also do #OATH, JWT
                 ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}