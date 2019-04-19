from django.urls import path
from archive import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.PostCreateView.as_view(success_url="/"), name='post_create'),
    path('delete/<pk>', views.PostDelete.as_view(), name="delete_post"),
]
