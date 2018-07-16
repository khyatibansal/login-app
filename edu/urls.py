from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name='edu'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$',login,{'template_name': 'edu/login.html'}),
    url(r'^logout/$',logout,{'template_name': 'edu/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^student/$',views.StudentView.as_view(),name='student_details'),
    url(r'^student/entry/$',views.StudentEntry.as_view(),name='student-entry'),
    url(r'^student/(?P<pk>[0-9]+)/$',views.StudentUpdate.as_view(),name='student-update'),
    url(r'^student/(?P<pk>[0-9]+)/delete$',views.StudentDelete.as_view(),name='student-delete'),




]