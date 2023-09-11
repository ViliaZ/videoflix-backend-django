from django.contrib import admin
from django.urls import path, include
from users import urls
from rest_framework import routers
from users.views import RegisterViewset

router = routers.DefaultRouter()
router.register(r'register', RegisterViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('account/', include(urls)),
    path('admin/', admin.site.urls),
]
