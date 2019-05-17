from users.api.views.FriendView import FriendViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<username>[-\w]+)', FriendViewSet, base_name='user')
urlpatterns = router.urls
