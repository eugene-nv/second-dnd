from rest_framework.routers import SimpleRouter

from .views import CharacterViewSet

router = SimpleRouter()

router.register(r'character', CharacterViewSet)

urlpatterns = []

urlpatterns += router.urls