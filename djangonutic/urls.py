from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
# from contact import views as contact_veiws
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    path('', include("contact.urls"), name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include("accounts.urls")),
    path('articles/', include("articles.urls"), name='articles'),
    path('contact/', include("contact.urls"), name='contact'),
    path('404/', views.view_404, name='404'),
    path('manifest.json', views.view_manifest_json, name='manifest'),
    path('robots.txt', views.view_robot_txt, name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    # path('', views.homepage),
    # path('', include("articles.urls")),



]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
