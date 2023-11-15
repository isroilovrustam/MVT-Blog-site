from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['blog']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for kalit, qiymat in self.fields.items():
            qiymat.widget.attrs['class'] = 'form-control'
