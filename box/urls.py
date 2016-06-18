from django.conf.urls import url
from box import views



urlpatterns = [
    url(r'^login_view/', views.login_view, name='login_view'),

]

