from django.urls import path

from . import views as car_api_views



urlpatterns = [
    path('create/', car_api_views.CreateAnnouncementAPIView.as_view(), name='create_announcement'),
]
