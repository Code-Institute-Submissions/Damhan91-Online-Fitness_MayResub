from . import views
from .views import CommentDeleteView
from django.urls import path


urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.home, name='home'),
    path('nutrition', views.nutrition, name='nutrition'),
    path('exercises', views.exercises, name='exercises'),
    path('like/<slug:slug>/', views.PostLikes.as_view(), name='post_likes'),
    path('<pk>/delete/', views.CommentDeleteView.as_view(), name='CommentDeleteView'),
    path('<pk>/edit/', views.EditComment.as_view(), name='EditComment')
]
