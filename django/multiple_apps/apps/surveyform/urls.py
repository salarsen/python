from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^this_app/surveys/process$',views.process,name='process')
]
