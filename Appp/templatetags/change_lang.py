from django import template

register = template.Library()


@register.filter(name='change_lang')
def change_lang(request, lang):
    url = str(request.path).split('/')
    url[1] = lang
    return '/'.join(url)
