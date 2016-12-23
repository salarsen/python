from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^this_app/register$',views.register_user,name='register_user'),
	url(r'^this_app/login$',views.login_user,name='login_user'),
	url(r'^this_app/logout',views.logout_user,name='logout_user'),
]
