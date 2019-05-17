from users.api.views.ProfileView import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProfileViewSet, base_name='profile')
urlpatterns = router.urls
