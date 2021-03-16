from django.urls import path
from . import views_2

app_name = "blog"


urlpatterns = [
    path("", views_2.all_blogs, name="all_blogs"),
    path("<int:blog_id>/", views_2.detail, name="detail"),
]


