from django.contrib import messages
from django.core.urlresolvers import reverse
from social_auth.exceptions import AuthAlreadyAssociated, AuthCanceled, AuthFailed
from social_auth.middleware import SocialAuthExceptionMiddleware



class AuthException(SocialAuthExceptionMiddleware):
    """docstring for AuthException"""

    def raise_exception(self, request, exception):
        return False

    def get_message(self, request, exception):
        msg = None
        if isinstance(exception, AuthFailed):
            msg = 'failed'
        elif isinstance(exception, AuthCanceled):
            msg = 'cancelled'
        elif isinstance(exception, AuthAlreadyAssociated):
            msg = 'registered'
        else:
            msg = 'other'
        print msg
        messages.add_message(request, messages.ERROR, msg)

    def get_redirect_uri(self, request, exception):
        if request.user.is_authenticated():
            return reverse('success')
        else:
            return reverse('errors')