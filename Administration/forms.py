from django import forms
from News.models import Interview, News
from ckeditor.fields import RichTextField

class NewNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('headline', 'image', 'summary', 'text')


class AddInterviewForm(forms.ModelForm):
	class Meta:
		model = Interview
		fields = ('title', 'thumbnail','event_date', 'description', 'video')