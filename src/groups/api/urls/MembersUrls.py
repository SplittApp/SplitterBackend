from groups.api.views.MembersView import MembersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MembersViewSet, base_name='member_user')
urlpatterns = router.urls
