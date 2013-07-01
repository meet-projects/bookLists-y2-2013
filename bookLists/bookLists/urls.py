from django.conf.urls import patterns, include, url
from books import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
        url(r'^$', views.home, name='home'),

        url(r'^categories/(?P<genre>\w+)/$',
            views.get_Books),
        
                       
    # url(r'^bookLists/', include('bookLists.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
