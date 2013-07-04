try:
    import markdown2
    markdown2_available = True
except ImportError:
    markdown2_available = False


if markdown2_available:
    from django import template
    from django.utils.safestring import mark_safe

    register = template.Library()

    @register.filter(is_safe=True, needs_autoescape=False)
    def markdown(value):
        return mark_safe(markdown2.markdown(value))
