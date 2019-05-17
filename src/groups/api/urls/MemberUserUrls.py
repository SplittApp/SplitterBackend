from groups.api.views.MemberUserView import MemberUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<username>[-\w]+)', MemberUserViewSet, base_name='member_user')
urlpatterns = router.urls
