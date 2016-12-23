from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^this_app/courses/add$',views.add_course,name='add_course'),
    url(r'^this_app/courses/destroy/(?P<id>\d+)$',views.destroy_course,name='destroy_course'),
    url(r'^this_app/courses/delete/(?P<id>\d+)$',views.delete_course,name='delete_course'),
	url(r'^this_app/courses/enrolled$',views.enrolled,name='enrolled'),
	url(r'^this_app/course/add_enrolled$',views.add_enrolled,name='enroll_user'),
]
