from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import ShortURL

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Linkit URL Shortener",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Linkit URL Shortener",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            template = "shortener/shorturl.html"
            return render(request, template, context)
        else:
            # Redirect to the same page to display the form with an empty form
            return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        if not obj.url.startswith("http://") and not obj.url.startswith("https://"):
            obj.url = "http://" + obj.url
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
