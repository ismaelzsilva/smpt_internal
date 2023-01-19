from django.urls import path
from . import views

app_name = 'labels'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('of/<pk>', views.OF.as_view(), name='of'),
    path('create_of', views.CreateOF.as_view(), name='create_of'),
    path('delete_of/<pk>', views.DeleteOF.as_view(), name='delete_of'),
    path('create_labels', views.CreateLabels.as_view(), name='create_labels'),
#     path('labels_pdf', views.LabelsPDF.as_view(), name='labels_pdf'),
]
