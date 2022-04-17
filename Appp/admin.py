from django.contrib import admin
from parler import admin as parler_admin
from .models import Slider, News, Images, contactModel, Linklar, reytinglar, About, num


# korsatgichlar

# korsatgichlar, FoydaiLinklar

# from myapp.models import Author

# admin.site.register(Author)
# Register your models here.
class adminParler(parler_admin.TranslatableAdmin):
    pass


class adminParlerNews(parler_admin.TranslatableAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'time']
    # list_filter = ['title', 'name']
    list_display_links = ['id', "title", 'time']


class adminParlerRetinglar(parler_admin.TranslatableAdmin, admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', "title"]


admin.site.register(Slider, adminParler)
admin.site.register(News, adminParlerNews)
admin.site.register(Images)
admin.site.register(contactModel)
admin.site.register(Linklar, adminParler)
admin.site.register(reytinglar, adminParlerRetinglar)
admin.site.register(num)
admin.site.register(About, adminParler)
