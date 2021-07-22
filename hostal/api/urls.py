from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'huespedes', views.HuespedViewSet)
router.register(r'clientes', views.ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login),
    url(r'^auth/login/$',obtain_auth_token, name='auth_user_login'),
    url(r'^auth/logout/$',views.LogoutUserAPIView.as_view(), name='auth_user_logout'),
    #path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
