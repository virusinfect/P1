"""
URL configuration for P1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views, admin_views, founder_views ,category_view
from django.conf import settings
from django.conf.urls.static import static
from app.views import SetLanguageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timeline/', views.timeline, name='timeline'),
    path('founders/', founder_views.founders_list, name='founders'),
    path('founderbio/<int:founder_id>/', founder_views.founderbio, name='founderbio'),
    path('login/', views.login, name='login'),
    path('sports/<int:main_category_id>/', category_view.subcategories_list, name='sports'),
    path('video/', views.video, name='video'),
    path('album/', views.album, name='video'),
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('set_language/<str:lang_code>/', SetLanguageView.as_view(), name='set_language'),
    path('backend/', admin_views.backend, name='backend'),
    path('add_founders/', admin_views.add_founders, name='add_founders'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)