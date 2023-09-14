
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import RegisterViewset
from users.views import LoginViewset, LogoutViewset

router = routers.DefaultRouter()
router.register(r'register', RegisterViewset, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginViewset.as_view(), name='login'),
    path('logout/', LogoutViewset.as_view(), name='logout'),
    path('admin/', admin.site.urls)
]
