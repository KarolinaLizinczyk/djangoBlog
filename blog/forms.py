from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('user', "slug", 'height_field', 'width_field')
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control'}),
            "img": forms.FileInput(attrs={'class': 'form-control'}),
            "draft": forms.CheckboxInput(),
            "publish": forms.DateTimeInput(attrs={'class': 'form-control'}),
        }


