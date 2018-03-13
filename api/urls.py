from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^test/$', views.TestView.as_view()),
    url(r'^testpost/$', views.TestPost.as_view())
]