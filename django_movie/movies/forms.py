from django import forms
from movies.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'reviews__message_box',
                                                                     'style': 'max-height: 300px; width: 600px',
                                                                     'placeholder': 'Comment text',
                                                                     }))

    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'reviews__message_box'})
        }
