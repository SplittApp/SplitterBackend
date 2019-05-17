from groups.api.views.MemberView import MemberViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<username>[-\w]+)', MemberViewSet, base_name='member')
urlpatterns = router.urls
