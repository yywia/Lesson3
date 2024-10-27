"""
URL configuration for game_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from gamestore import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('publishers', views.PublisherAPI, basename='publishers')
router.register('games', views.GameAPI, basename='games')
router.register('developers', views.DeveloperAPI, basename='developers')
router.register('genres', views.GenreAPI, basename='genres')
router.register('statistics', views.StatisticsAPI, basename='statistics')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),

    path('games_list/', views.GamesList.as_view(), name='games_list'),
    path('games/<int:pk>/', views.GamesDetail.as_view(), name='games_detail'),
    path('games/<int:pk>/update/', views.GamesUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GamesDelete.as_view(), name='games_delete'),
    path('games/create/', views.GamesCreate.as_view(), name='game_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
