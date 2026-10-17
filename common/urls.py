from django.urls import path

from common import views
from common.views import SearchResultView, ProfileView

app_name = 'common'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', SearchResultView.as_view(), name='search'),
    path('profile', ProfileView.as_view(), name='profile'),
]