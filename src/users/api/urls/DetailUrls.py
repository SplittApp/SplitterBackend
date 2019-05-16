from users.api.views.DetailView import DetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', DetailViewSet, base_name='user_detail')
urlpatterns = router.urls
