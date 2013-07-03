from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def ordering_link(context, field):
    request = context.get('request', None)
    if request is None:
        return ''

    sort_get = request.GET.get('sort', '')
    icon_base = '<i class="icon-chevron-%s"></i>'
    icon = 'up'
    sort = field
    if not ("-%s" % field in sort_get) and (field in sort_get):
        sort = '-%s' % field
        icon = "down"
    icon_base %= icon
    return '<a href="?page=1&sort=%s">%s</a>' % (sort, icon_base)
