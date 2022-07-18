from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, ReviewViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]