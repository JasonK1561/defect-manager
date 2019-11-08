from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,DetailView,UpdateView,
                                    CreateView)
from defect_manager_app.models import Defect,Comment
from defect_manager_app.forms import DefectForm, CommentForm
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

# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm


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
