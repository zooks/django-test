from django.conf.urls import include, url
from django.contrib import admin
from main.views import home, item, get_category
# from main import views as main_views


urlpatterns = [
    # Examples:
    # url(r'^$', 'futbolkas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^item/(?P<alias>[^/]+)', item, name='item'),
    url(r'^(?P<alias>[^/]+)', get_category, name='get_category'),
    url(r'^$', home, name='home'),
]
