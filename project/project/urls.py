"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import app.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name='index'),
    path('board1/', app.views.board1, name='board1'),
    path('board1/<int:pk>/', app.views.posting, name='posting'),
    path('board1/new_post/', app.views.new_post),
    path('board1/<int:pk>/delete', app.views.board_delete, name='board_delete'),
    path('board1/<int:pk>/edit', app.views.board_edit, name='board_edit'),
    path('board2/', app.views.board2, name='board2'),#not yet
    path('board2/<int:pk>/', app.views.posting, name='posting'),
    path('board2/new_post/', app.views.new_post),
    path('board2/<int:pk>/delete', app.views.board_delete, name='board_delete'),
    path('board2/<int:pk>/edit', app.views.board_edit, name='board_edit'),
    path('board3/', app.views.board3, name='board3'),#not yet
    path('board3/<int:pk>/', app.views.posting, name='posting'),
    path('board3/new_post/', app.views.new_post),
    path('board3/<int:pk>/delete', app.views.board_delete, name='board_delete'),
    path('board3/<int:pk>/edit', app.views.board_edit, name='board_edit'),
    path('login', app.views.login, name="login")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
