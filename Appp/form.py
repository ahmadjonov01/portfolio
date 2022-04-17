from .models import contactModel
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = contactModel
        fields = '__all__'


from django.views.generic import ListView

from .models import Images


class ImagesListView(ListView):
    paginate_by = 1
    model = Images


from .models import News


class NewsListView(ListView):
    paginate_by = 2
    model = News
