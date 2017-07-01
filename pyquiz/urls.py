from django.conf.urls import url

from . import views

app_name = 'pyquiz'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
    url(r'^question/(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer')
]
