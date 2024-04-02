from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/', obtain_auth_token),  # Obtain authentication token URL
    path('api/', include('messaging_system.urls')),  # Include messaging system app URLs
]
