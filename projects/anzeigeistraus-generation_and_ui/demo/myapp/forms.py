from django import forms

class ChatForm(forms.Form):
    query = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Was kann ich für Sie tun?',
            'rows': 4,
            'class': 'chat-input'
        })
    )