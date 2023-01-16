from django.urls import path 
from . import views

urlpatterns = [
    path('dashboard',views.doctorDashboard,name='doctorDashboard'),
    path('manage',views.manageView,name='manageView'),
    path('convert',views.convertView,name='convertView'),
    path('patients',views.patientView,name='patientView'),
    path('test',views.testView,name='testView'),
    path('test/<int:id>',views.testdetailView,name='testdetailView'),
    path('add',views.addPatientView,name='addPatientView'),
    path('delete/<int:id>',views.deleteView,name='deleteView'),
]
