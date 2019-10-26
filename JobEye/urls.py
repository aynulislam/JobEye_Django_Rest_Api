from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('buyer/', include('buyer_app.urls')),
    path('admin/', admin.site.urls),
    path('job/', include('job_app.urls')),
    path('worker/', include('worker_app.urls')),
    path('test/', include('test_app.urls')),
    path('application/', include('application_app.urls')),
    path('general/', include('general_app.urls')),
]
