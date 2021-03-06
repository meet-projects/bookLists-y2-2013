from django.conf.urls import patterns, include, url
from books import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
        url(r'^$', views.home, name='home'),
        url(r'^home$', views.home),
	url(r'^books/(?P<book>[\w \']+)/$', views.get_book),
	url(r'^market$' , views.market),
        url(r'^books/(?P<bookName>[\w \']+)/submitrating$', views.submitRating),
        url(r'^categories/(?P<genre>\w+)/$', views.get_genre),
        url(r'^submitlogin$', views.submitlogin),
        url(r'^submitregister$', views.register),
        url(r'^signup$', views.sign_up),
        url(r'^submitlogout$', views.submitlogout),
        url(r'^profile$', views.get_profile),
        url(r'^uploadImage$', views.uploadPage),
        url(r'^search$', views.search),
        url(r'^profiles/(?P<email>[\w\.\@]+)$', views.get_others_profile), 
        url(r'^addComment$', views.addComment), 
       # url(r'^?search=(?p<ask>[\w \']+)/$', views.search)
                       
    # url(r'^bookLists/', include('bookLists.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
