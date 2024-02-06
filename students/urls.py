from django.urls import path
from students.views import StudentListCreate, StudentRetrieveUpdateDestroy

urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroy.as_view(), name='student-detail'),
]
