from django.urls import path

from . import views

urlpatterns = [
    path('marksheets/',views.marksheets,name='marksheets'),
      path('studentmark/<int:pk>',views.studentmark,name='studentmark'),

]
