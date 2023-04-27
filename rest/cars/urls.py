from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

app_name = "cars"
router = routers.SimpleRouter()
router.register(r'', CarViewSet, basename='cc')

urlpatterns = [
    # path('', views.all_category, name='all_category'),
    path('', CarAPIList.as_view()),
    path('<int:pk>/', CarAPIViews.as_view()),
    path('api/', include(router.urls)),
    # path('', views.index_html, name='index_html'),
    # path('s/', ProfileList.as_view()),
]