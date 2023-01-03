from django.db import models
from django.conf import settings

from django_hosts.resolvers import reverse

# Create your models here

from .utils import create_shortcode

from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    # Destroys all previous shortcodes and refreshes everything with new ones.
    def refresh_shortcodes(self, items=100):
        qs = ShortURL.objects.filter(id__gte=1)
        new_codes = 0
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save
            new_codes += 1
        return f"New codes made: {new_codes}"


class ShortURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ShortURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=="":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        # use this version during production
        # url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme="http")
        url_path = "http://127.0.0.1:8000/" + self.shortcode
        return url_path


'''
python manage.py makemigrations
python manage.py migrate
^ for whenever updating models.py

You can delete migrations and db.sqlite3 and run
python manage.py createsuperuser to reset it all

'''