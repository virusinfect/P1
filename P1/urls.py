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
from app import views,founder_views ,category_view, video_views
from django.conf import settings
from django.conf.urls.static import static
from app.views import SetLanguageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timeline/', views.timeline, name='timeline'),
    path('founders/', founder_views.founders_list, name='founders'),
    path('chairmans/', founder_views.chairmans_list, name='chairmans'),
    path('founderbio/<int:founder_id>/', founder_views.founderbio, name='founderbio'),
    path('chairmanbio/<int:chairman_id>/', founder_views.chairmanbio, name='chairmanbio'),
    path('login/', views.login, name='login'),
    path('sports/<int:main_category_id>/', category_view.subcategories_list, name='sports'),
    path('video/', video_views.video_list, name='videolist'),
    path('add-comment/<int:photo_id>/', category_view.add_comment, name='add_comment'),
    path('events', category_view.event_category_view, name='events'),
    path('project', category_view.project_category_view, name='project'),
    path('senior/<int:main_category_id>/', category_view.senior_category_detail, name='senior'),
    path('video-player/<int:video_id>/', video_views.video_player, name='video_player'),
    path('album/<int:child_category_id>/', category_view.child_category_images, name='album'),
    path('get-comments/', category_view.get_comments, name='comments'),
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('pdf/<int:pdf_id>/', views.pdf, name='pdf'),
    path('books/', views.book_list, name='book_list'),
    path('set_language/<str:lang_code>/', SetLanguageView.as_view(), name='set_language'),
    path('get-comment-count/', category_view.get_comment_count, name='get_comment_count'),
    path('75years/<int:video_id>/', video_views.celebration_video, name='75years'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)