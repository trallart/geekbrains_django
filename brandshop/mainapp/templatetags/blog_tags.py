from django import template

register = template.Library()


@register.simple_tag
def url_params(name, value, params=None):
# def url_params(name):
#     print('+'*100, 'Ура я попал сюда')
#     print('Имя', name)
#     print('Значение', value)
#     print('Параметр', params)
    url = '?' + name + '=' + value
    if params:
        qs = '&'.join(p for p in params.split('&') if p.split('=')[0] != name)
        url = url + '&' + qs
    # print(url)
    return url