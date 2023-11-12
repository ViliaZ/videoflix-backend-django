from django.contrib import admin
from .models import Movie
from import_export.admin import ImportExportModelAdmin

# add import/export Option in Admin Panel
class MovieResource(ImportExportModelAdmin):
    model = Movie
    
admin.site.register(Movie, MovieResource)