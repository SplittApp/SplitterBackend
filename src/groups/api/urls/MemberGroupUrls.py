from groups.api.views.MemberGroupView import MemberGroupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<reference>[-\w]+)', MemberGroupViewSet, base_name='member_group')
urlpatterns = router.urls
