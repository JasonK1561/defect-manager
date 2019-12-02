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
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class DefectListView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Defect

class DefectDetailView(LoginRequiredMixin, DetailView):
    model = Defect

class DefectUpdateView(LoginRequiredMixin, UpdateView):
    model = Defect
    form_class = DefectForm
    # fields = ['notes','name', 'severity', 'defect_type', 'defect_status']
    redirect_field_name = 'defect_manager_app/defect_detail.html'

class DefectCreateView(LoginRequiredMixin, CreateView):
    model = Defect
    form_class = DefectForm


class DefectDeleteView(LoginRequiredMixin, DeleteView):
    model = Defect
    success_url = reverse_lazy('defect_manager_app:defect_list')
# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm
class ClosedDefectListView(LoginRequiredMixin, ListView):
    model = Defect
    template_name = 'defect_manager_app/closed_defect_list.html'

def create_comment(request, pk):
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
