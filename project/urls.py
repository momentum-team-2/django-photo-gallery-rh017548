"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from core import views as core_views
from django.conf.urls import include

urlpatterns = [
    path('', core_views.home, name='home'),
    path('core/', core_views.list_photo, name='list_photo'),
    path('core/add/', core_views.add_photo, name='add_photo'),
    path('core/<int:pk>/edit/', core_views.edit_photo, name='edit_photo'),
    path('core/<int:pk>/delete/', core_views.delete_photo, name='delete_photo'),
    path('core/<int:pk>/show', core_views.show_photo, name = 'show_photo'),
    path('albums/', core_views.list_album, name='list_album'),
    path('albums/add/', core_views.add_album, name='add_album'),
    path('albums/<int:pk>/', core_views.show_album, name='show_album'),
    path('albums/<int:pk>/edit/', core_views.edit_album, name='edit_album'),
    path('albums/<int:pk>/delete/', core_views.delete_album, name='delete_album'),
    path('albums/<int:pk>/add/photo/', core_views.add_photo_to_album, name='add_photo_to_album'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api/', include('api.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
