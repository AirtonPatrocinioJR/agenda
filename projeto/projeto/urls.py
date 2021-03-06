from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
#import djangowars.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'usuario.views.index', name='usuario_index'),
    url(r'^sair/$', 'usuario.views.sair', name='usuario_sair'),
    url(r'^cadastrar/$', 'usuario.views.registrar', name='usuario_registrar'),
    #url(r'^$', 'agenda.views.index', name='home'),
    # url(r'^projeto/', include('projeto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

#if settings.DEBUG:
#	urlpatterns += patterns('',
#		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#		{'document_root': settings.MEDIA_ROOT, 'show_indexes':True})
#	)
#
#urlpatterns += staticfiles_urlpatterns()