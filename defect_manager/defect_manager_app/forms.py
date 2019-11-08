from django import forms
from defect_manager_app.models import Defect, Comment

class DefectForm(forms.ModelForm):

    class Meta:
        model = Defect

        fields = ('notes', 'name', 'severity', 'defect_type', 'defect_status')

        widgets = {
            'notes': forms.TextInput(attrs={'class': 'textinputclass'}),
            'name': forms.TextInput(attrs={'class': 'nameinputclass'}),
            'severity': forms.Select(attrs={'class': 'dropdownclass'}, choices=Defect.DEFECT_SEVERITY_CHOICES),
            'defect_type': forms.Select(attrs={'class': 'dropdownclass'}, choices=Defect.DEFECT_TYPE_CHOICES),
            'defect_status': forms.Select(attrs={'class': 'dropdownclass'}, choices=Defect.DEFECT_STATUS_CHOICES),
        }


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ('author', 'text')

        widgets = {
            'text': forms.TextInput(attrs={'class': 'textinputclass'})
        }
