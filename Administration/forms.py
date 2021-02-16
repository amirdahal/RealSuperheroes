from django import forms
from News.models import News
from ckeditor.fields import RichTextField

class NewNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('headline', 'image', 'summary', 'text')

