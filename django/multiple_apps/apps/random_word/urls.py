from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^this_app/gen_word$',views.new_word,name='new_word')
]
