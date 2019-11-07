from django.urls import path
from defect_manager_app import views

app_name = 'defect_manager_app'

urlpatterns = [
    path('', views.DefectListView.as_view(), name='defect_list'),
    path('detail/<int:pk>',views.DefectDetailView.as_view(), name='defect_detail'),
    path('update/defect/<int:pk>', views.DefectUpdateView.as_view(), name='update_defect'),

]
