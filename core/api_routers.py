from django.urls import include, path

urlpatterns = [
    path('cars/', include('cars.api.urls'))
]