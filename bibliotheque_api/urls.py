from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LivreViewSet, RegisterView, LoginView, MeView

router = DefaultRouter()
router.register(r'livres', LivreViewSet, basename='livre')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
]

urlpatterns += router.urls
