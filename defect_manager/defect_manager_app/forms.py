from django import forms
from defect_manager_app.models import Defect, Comment

class DefectForm(forms.ModelForm):

    class Meta:
        model = Defect

        fields = ('author','name', 'severity', 'defect_type', 'defect_status', 'notes')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'nameinputclass all-widgets'}),
            'name': forms.TextInput(attrs={'class': 'nameinputclass all-widgets'}),
            'notes': forms.Textarea(attrs={'class': 'textinputclass all-widgets'}),
            'severity': forms.Select(attrs={'class': 'dropdownclass all-widgets'}, choices=Defect.DEFECT_SEVERITY_CHOICES),
            'defect_type': forms.Select(attrs={'class': 'dropdownclass all-widgets'}, choices=Defect.DEFECT_TYPE_CHOICES),
            'defect_status': forms.Select(attrs={'class': 'dropdownclass all-widgets'}, choices=Defect.DEFECT_STATUS_CHOICES),
        }


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ('author', 'text')

        widgets = {
            'text': forms.TextInput(attrs={'class': 'textinputclass'})
        }

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
