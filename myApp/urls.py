from rest_framework.routers import DefaultRouter
from .api import PagoCreateRetrieveUpdateListViewSet

user_router = DefaultRouter()

user_router.register(r"pagos", PagoCreateRetrieveUpdateListViewSet, basename="pagos")
urlpatterns = user_router.urls