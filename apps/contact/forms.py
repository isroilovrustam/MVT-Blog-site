from django import forms
from .models import Contact, Subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for kalit, qiymat in self.fields.items():
            qiymat.widget.attrs['class'] = 'form-control'


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        for kalit, qiymat in self.fields.items():
            qiymat.widget.attrs['class'] = 'form-control'
