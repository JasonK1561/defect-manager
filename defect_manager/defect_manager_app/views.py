from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,UpdateView,
                                    CreateView, DeleteView)
from defect_manager_app.models import Defect,Comment
from defect_manager_app.forms import DefectForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
# Create your views here.
class SignUp(CreateView):
    """View for user sign up"""
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class DefectListView(LoginRequiredMixin, ListView):
    """List of defect view"""
    login_url = 'accounts/login/'
    model = Defect

class DefectDetailView(LoginRequiredMixin, DetailView):
    """Defect detail view of an instance of a defect"""
    model = Defect

class DefectUpdateView(LoginRequiredMixin, UpdateView):
    """Form view for a defect instance for updating"""
    model = Defect
    form_class = DefectForm
    # fields = ['notes','name', 'severity', 'defect_type', 'defect_status']
    redirect_field_name = 'defect_manager_app/defect_detail.html'

class DefectCreateView(LoginRequiredMixin, CreateView):
    """Form view for creating a defect instance"""
    model = Defect
    form_class = DefectForm


class DefectDeleteView(LoginRequiredMixin, DeleteView):
    """Deleting a defect instance"""
    model = Defect
    success_url = reverse_lazy('defect_manager_app:defect_list')

#Initially tried to create a create view for creating a comment
# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm
class ClosedDefectListView(LoginRequiredMixin, ListView):
    """View for list of closed defects"""
    model = Defect
    template_name = 'defect_manager_app/closed_defect_list.html'

def create_comment(request, pk):
    """Function view for creating a comment on a defect instance"""
    defect = get_object_or_404(Defect, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.defect = defect
            comment.save()
            return redirect('defect_manager_app:defect_detail', pk=defect.pk)
    else:
        form = CommentForm()

    return render(request, 'defect_manager_app/comment_form.html', {'form':form})
