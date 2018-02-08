from django.conf.urls import url

from users import views


urlpatterns = [
    url(r'^login/', views.CreateUser.as_view()),
    url(r'^upload/', views.UploadImage.as_view()),
    url(r'^fetch/', views.FetchNearby.as_view()),
]
