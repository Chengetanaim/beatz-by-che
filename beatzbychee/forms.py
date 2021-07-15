from django import forms
from .models import MessageTopic


class MessageTopicForm(forms.ModelForm):
    class Meta:
        model = MessageTopic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


