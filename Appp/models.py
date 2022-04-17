from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField
from django.utils import translation
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class num(models.Model):
    n = models.CharField(max_length=1)


class Slider(TranslatableModel):
    class Meta:
        verbose_name = "Slider"

    translations = TranslatedFields(
        title=models.CharField(max_length=50),
        text=models.TextField()
    )
    image = models.FileField(upload_to='static/images_slider')
    link = models.CharField(max_length=2000, verbose_name=_('Link'))

    def __str__(self):
        return self.title


class News(TranslatableModel):
    class Meta:
        verbose_name = "News"

    translations = TranslatedFields(
        title=models.CharField(max_length=2000),
        sub_title=models.CharField(max_length=2000),
        text=models.TextField()
    )
    image = models.FileField(upload_to="static/images_news")
    time = models.DateField(blank=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    class Meta:
        verbose_name = "Image"

    image = models.FileField(upload_to='static/images_photos')

    def __str__(self):
        return str(self.id)


class contactModel(models.Model):
    phone = models.CharField(max_length=14)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return str(self.id) + ') ' + self.name


# class korsatgichlar(TranslatableModel):
#     translations = TranslatedFields(
#         title=models.TextField(verbose_name=_('Title'))
#     )
#     link = models.TextField()
#     datetime = models.DateField(verbose_name=_('Yuklanga vaqti'))
#     ico = models.CharField(max_length=2000, verbose_name=_('Icon class'))

#     def __str__(self):
#         return str(self.id) + ')' + self.title
class reytinglar(TranslatableModel):
    class Meta:
        verbose_name = 'Ko`rsatgichlar'

    translation = TranslatedFields(
        title=models.CharField(max_length=30300, verbose_name=_("Title"))
    )
    reytingnatijasi = models.CharField(max_length=200000, verbose_name=_('Natijasi'))
    icon = models.CharField(max_length=2000, verbose_name=_("Icon belgisi"))
    data = models.DateField(auto_now_add=True, verbose_name=_('Vaqti'))


class Linklar(TranslatableModel):
    class Meta:
        verbose_name = 'Foydali Linklar'

    translations = TranslatedFields(
        title=models.TextField(verbose_name=_('Title'))
    )
    link = models.TextField(verbose_name=_('Havolasi'))
    datetime = models.DateField(verbose_name=_('Yuklanga vaqti'))
    icon = models.CharField(max_length=2000, verbose_name=_('Icon class'))

    def __str__(self):
        return str(self.id) + ')' + self.title


class About(TranslatableModel):
    class Meta:
        verbose_name = 'Malumotalar'

    translation = TranslatedFields(
        title=models.CharField(max_length=20000, verbose_name=_('Title')),
        text=models.TextField(verbose_name=_('Text'))
    )
    datatime = models.DateField(verbose_name=_('Vaqti'))
    image = models.ImageField(verbose_name=_("Image"), upload_to="static/images")

    # datetime = models.DateField(verbose_name=_('Yuklanga vaqti'))

    def __str__(self):
        return str(self.id) + ')' + self.title
