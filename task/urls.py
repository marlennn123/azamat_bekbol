from django.urls import path
from .views import FacultyViewSet, ProfessorViewSet,StudentViewSet, CourseViewSet


urlpatterns = [
    path('', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}), name='Faculty_list'),
    path('<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='Faculty_detail'),


    path('Professor/', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='Professor_list'),
    path('Professor/<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='Professor_detail'),


    path('Student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='Student_list'),
    path('Student/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='Student_detail'),


    path('Course/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='Course_list'),
    path('Course/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='Course_detail')

]