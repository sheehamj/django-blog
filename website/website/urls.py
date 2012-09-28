from django.conf.urls import patterns, include, url

from website.blog.models import Entry
from tagging.views import tagged_object_list

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

info_dict = {

	'queryset': Entry.objects.filter(status=1),

	'date_field': 'pub_date',

}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.views.generic.date_based.archive_index', dict(info_dict, template_name='main/list.html')),
    url(r'^blog/', include('website.blog.urls')),
    #url(r'^tags/', include('website.tagging.urls')),
    url(r'^tags/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'website.tag_views.tag_detail'),
    url(r'^blog/tags/','website.blogtag_views.tag_detail'),
    url(r'^about/', 'django.views.generic.date_based.archive_index', dict(info_dict, template_name='about/list.html')),     

)
