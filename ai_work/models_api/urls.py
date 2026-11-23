from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ModelAuthorViewSet, AIModelViewSet, ModelPurchaseViewSet,
                    UsageScenarioViewSet, ModelBenchmarkViewSet)

router = DefaultRouter()
router.register(r'authors', ModelAuthorViewSet)
router.register(r'models', AIModelViewSet)
router.register(r'purchases', ModelPurchaseViewSet)
router.register(r'usage-scenarios', UsageScenarioViewSet)
router.register(r'benchmarks', ModelBenchmarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]