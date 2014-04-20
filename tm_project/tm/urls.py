from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'tm.views.home'),
    url(r'^showthumbnail', 'tm.views.show_thumbnail'),
    url(r'^geteventlist', 'tm.views.get_event_list'),
    url(r'^getphotolist', 'tm.views.get_photo_list'),
    url(r'^getphoto', 'tm.views.get_photo'),
    url(r'^showevent', 'tm.views.show_event'),
    url(r'^getcomments', 'tm.views.get_comments'),
    url(r'^getlabels', 'tm.views.get_labels'),
    



)
