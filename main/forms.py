from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    """ A comment from a user which may be in response to blog post. """

    class Meta:
        model = Comment
        fields = ['name', 'email', 'message', 'copy_sent']

        labels = {
            'copy_sent': 'Send me a copy'
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'required': True,
            }),
            'copy_sent': forms.CheckboxInput(attrs={
                'class': 'form-check-input mx-2',
                'required': False,
                'label': 'Send me a copy'
            })
        }



