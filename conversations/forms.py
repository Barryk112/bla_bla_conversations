from .models import Comment, ConversationPost
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class ConversationForm(forms.ModelForm):
    
    class Meta:
        model = ConversationPost
        fields = (
            'title',
            'featured_image',
            'content',
            'status'
        )