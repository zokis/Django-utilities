from django.forms.widgets import TextInput


class TelefoneWidget(TextInput):

    def __init__(self, attrs=None):
        attrs_default = {'placeholder': 'xx-(x)xxxx-xxxx', 'maxlength': 13}
        if attrs:
            attrs_default.update(attrs)
        super(TelefoneWidget, self).__init__(attrs=attrs_default)
