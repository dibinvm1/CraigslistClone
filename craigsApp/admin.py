from django.contrib import admin

from .models import Search

admin.AdminSite.site_header = "Craigslist "

admin.site.register(Search)

