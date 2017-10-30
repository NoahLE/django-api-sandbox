from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/$', include('rest_framework.urls'), name='rest_framework'),
]
