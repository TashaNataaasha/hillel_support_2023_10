from django.urls import path
from .api import activate_user

urlpatterns = [
    # Other endpoints...
    path('users/activate/', activate_user, name='activate_user'),
]