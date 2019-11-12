from django import forms
from defect_manager_app.models import Defect, Comment

class DefectForm(forms.ModelForm):

    class Meta:
        model = Defect

        fields = ('name', 'severity', 'defect_type', 'defect_status', 'notes')

        widgets = {
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
