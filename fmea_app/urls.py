from django.conf.urls import url
from fmea_app import views
from .views import CreatePostView # new
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^post/$', CreatePostView.as_view(), name='add_post') # new
]
