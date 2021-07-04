from django.urls import path
from home.views import  Index, delete_task, change_status, Upcoming

urlpatterns = [
    path('', Index, name = 'home'),
    path('delete_task/<int:id>', delete_task, name = 'delete_task'),
    path('change_status/<int:id>/<str:status>', change_status, name = 'change_status'),
    path('upcoming/', Upcoming, name = 'upcoming')
]