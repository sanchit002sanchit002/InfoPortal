from django.conf.urls import url


from users import views

# urlpatterns = [url(r'^$', views.index, name='index'),]
urlpatterns = [url(r'^$', views.users, name='users'),]
