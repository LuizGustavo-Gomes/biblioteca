from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, BibliotecarioViewSet, LivroViewSet, EmprestimoViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'bibliotecario', BibliotecarioViewSet)
router.register(r'livro', LivroViewSet)
router.register(r'emprestimo', EmprestimoViewSet)
router.register(r'reserva', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]