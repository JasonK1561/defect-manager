from django.urls import path
from defect_manager_app import views

app_name = 'defect_manager_app'

urlpatterns = [
    path('', views.DefectListView.as_view(), name='defect_list'),
    path('detail/<int:pk>',views.DefectDetailView.as_view(), name='defect_detail'),
    path('update/defect/<int:pk>', views.DefectUpdateView.as_view(), name='update_defect'),
    path('comment/defect/<int:pk>', views.create_comment, name='add_comment'),
    path('create/defect', views.DefectCreateView.as_view(), name='create_defect'),
    path('delete/defect/<int:pk>', views.DefectDeleteView.as_view(),name='delete_defect'),
    path('closed/', views.ClosedDefectListView.as_view(), name='closed_defect_list'),
]
