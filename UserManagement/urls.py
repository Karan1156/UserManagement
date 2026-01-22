from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet

# Create a router and register our viewset
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]