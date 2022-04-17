from django.core import paginator
from django.shortcuts import render
from .models import Slider, News, Images, Linklar, reytinglar, About, num
from .form import ContactForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import contactModel
import json

# <----TELEGRAMMBOT----->#

import requests


def send_message(text):
    token = '2035181861:AAFsSSluyloSGcdlDYK_I5Zodfw6V1NHZy4'
    chat_id = 1322649411

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text,
    }
    resp = requests.get(url, params=params)

    # Throw an exception if Telegram API fails
    resp.raise_for_status()


# Create your views here.

def index(request):
    data = Slider.objects.all()
    dataNews = News.objects.all()
    dataK = reytinglar.objects.all()
    dataF = Linklar.objects.all()
    context = {
        'data': data,
        'dataNews': dataNews,
        'photo': Images.objects.all(),
        'dataK': dataK,
        'dataF': dataF

    }
    return render(request, 'index.html', context)


def news(request):
    data = News.objects.all().order_by('?')
    paginator = Paginator(data, 3)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dataF = Linklar.objects.all()

    context = {
        'data': data,
        'page_obj': page_obj,
        'daatF': dataF,
    }
    return render(request, 'allNews.html', context)


def newsContent(request, id):
    data = News.objects.filter(id=id)
    dataall = News.objects.all().order_by('?')
    dataF = Linklar.objects.all()

    context = {
        "data": data,
        "dataall": dataall,
        'dataF': dataF,

    }

    return render(request, 'newsContent.html', context)


def photos(request):
    dataF = Linklar.objects.all()
    context = {
        'dataF': dataF
    }

    return render(request, 'allPhotos.html', context)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form: ContactForm = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.data.get('name')
            data1 = form.data.get('phone')
            data2 = form.data.get('email')
            data3 = form.data.get('company')
            data4 = form.data.get('message')

            send_message(f"Ism F.I.SH {data} Tel nomer 📱: {data1} email 📧:{data2} hudud: {data3}: message ✍:{data4}")

            return redirect('index')

    context = {
        'form': form
    }
    dataF = Linklar.objects.all()
    context = {
        'dataF': dataF
    }

    return render(request, 'contact.html', context)


def about(request):
    data = About.objects.all()
    dataF = Linklar.objects.all()

    context = {
        'data': data,
        'dataF': dataF

    }

    return render(request, 'about.html', context)


def gallery(request):
    dataF = Linklar.objects.all()
    data = Images.objects.all()

    paginator = Paginator(data, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'data': data,
        'dataF': dataF,
        'page_obj': page_obj
    }
    return render(request, 'gallery.html', context)


def base(request):
    dataF = Linklar.objects.all()
    context = {
        'dataF': dataF
    }

    return render(request, 'base.html', context)


def adoutsingel(request, id):
    datalar = About.objects.all()
    data = About.objects.filter(id=id)
    dataF = Linklar.objects.all()

    context = {
        'data': data,
        'datalar': datalar,
        'dataF': dataF

    }
    return render(request, 'aboutsingel.html', context)
