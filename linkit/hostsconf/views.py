from django.conf import settings
from django.http import HttpResponseRedirect

# DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.linkit.com/") # for production
DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL", "http://127.0.0.1:8000/")

def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)