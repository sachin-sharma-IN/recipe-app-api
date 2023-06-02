"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

app_name = "user"

# Any req. passed to `create/` will be handled by CreateUserView defined in user/view.py
# as_view() is used to convert class based view to supported Django view
# name='create' is used for reverse lookup in test cases.
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
