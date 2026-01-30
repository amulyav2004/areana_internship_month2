from django import forms
from .models import Group, GroupPost

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'image']

class GroupPostForm(forms.ModelForm):
    class Meta:
        model = GroupPost
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': "Share something with the group..."}),
        }
