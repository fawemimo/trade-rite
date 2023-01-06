from django.contrib.sitemaps import Sitemap
from .models import *


class TestimonialSitemap(Sitemap):
    def items(self):
        return Testimonial.objects.all()
