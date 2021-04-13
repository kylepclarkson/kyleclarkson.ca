from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea)


