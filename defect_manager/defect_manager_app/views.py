from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,UpdateView)
from defect_manager_app.models import Defect,Comment
from defect_manager_app.forms import DefectForm
# Create your views here.

class DefectListView(ListView):
    model = Defect

class DefectDetailView(DetailView):
    model = Defect

class DefectUpdateView(UpdateView):
    model = Defect
    form_class = DefectForm
    # fields = ['notes','name', 'severity', 'defect_type', 'defect_status']
    redirect_field_name = 'defect_manager_app/defect_detail.html'
