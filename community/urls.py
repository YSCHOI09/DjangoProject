from django.urls import path, re_path
from .views import write, list, view

urlpatterns = [
    path('write/', write, name='write'),
    path('list/', list, name='list'),
    re_path(r'^view/(?P<num>[0-9]+)/$', view, name='view'),
]
