from groups.api.views.GroupsView import GroupsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', GroupsViewSet, base_name='groups')
urlpatterns = router.urls
