from users.api.views.UserView import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, base_name='user')
urlpatterns = router.urls
