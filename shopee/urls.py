from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *




urlpatterns = [
    path('', ShopeeMarket.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('', cache_page(60)(ShopeeMarket.as_view()), name='home'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
