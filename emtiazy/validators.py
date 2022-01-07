from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class FacebookValidator:
    message = _('Enter a valid Facebook account.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if 'facebook' not in value:
            raise ValidationError(self.message, code=self.code, params={'value': value})


@deconstructible
class TwitterValidator:
    message = _('Enter a valid Twitter account.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if 'twitter' not in value:
            raise ValidationError(self.message, code=self.code, params={'value': value})


@deconstructible
class PhoneValidator:
    message = _('Enter a valid phone number.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if '+' not in value:
            raise ValidationError(self.message, code=self.code, params={'value': value})


@deconstructible
class InstagramValidator:
    message = _('Enter a valid Instagram account.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if 'instagram' not in value:
            raise ValidationError(self.message, code=self.code, params={'value': value})


@deconstructible
class PhoneValidator:
    message = _('Enter a valid phone number.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if '+' not in value:
            raise ValidationError(self.message, code=self.code, params={'value': value})


@deconstructible
class WhatsappValidator:
    message = _('Enter a valid Whatsapp account.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if 'whatsapp' not in value:
            raise ValidationError(self.message, code=self.code, params={'value': value})
