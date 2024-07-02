from django.urls import path
from .views import FacultyViewSet


urlpatterns = [
    path('', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}), name='task_list'),

    path('<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='task_detail')
]