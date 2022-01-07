"""emtiazyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, re_path, include
from django.views.generic import TemplateView, RedirectView
from django.views.static import serve

urlpatterns = [
    path('account-emtiazy/', admin.site.urls),
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico")), ),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('summernote/', include('django_summernote.urls')),
    path('api/', include('api.urls')),
]
urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^s/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT}),
    ]
