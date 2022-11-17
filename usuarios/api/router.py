from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from usuarios.api.views import UsuarioApiViewSet, UsuarioView

router_usuario = DefaultRouter()

router_usuario.register(
    prefix="usuarios", basename="usuarios", viewset=UsuarioApiViewSet
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/usuarioActual/', UsuarioView.as_view())
]
