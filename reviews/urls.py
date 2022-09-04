from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.ReviewView.as_view(), name='homepage'),
    path('thanks', views.ThankYou.as_view(), name='thanks'),
    path('reviews', views.Review_Lists.as_view(), name='reviews'),
    path('reviews/favorite', views.Favorite.as_view(), name='favorite_reviews'),
    path('reviews/<int:pk>', views.single_review.as_view(), name='review'),
]