
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import RegisterViewset
from users.views import LoginViewset, LogoutViewset, UserdataViewset
from django.conf import settings
from django.conf.urls.static import static
from content.views import MovieDetails

router = routers.DefaultRouter()
router.register(r'register', RegisterViewset, basename='register')
router.register(r'moviedetails', MovieDetails, basename='moviedetails')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginViewset.as_view(), name='login'),
    path('logout/', LogoutViewset.as_view(), name='logout'),
    path('userdetails/', UserdataViewset.as_view(), name='userdetails'),
    path('admin/', admin.site.urls)
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)