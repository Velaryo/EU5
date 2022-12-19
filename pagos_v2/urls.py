from rest_framework.routers import DefaultRouter
from .api import ServiceViewSet, PaymentUserViewSet, ExpiredPaymentViewSet

pagos_v2_router = DefaultRouter()
pagos_v2_router.register(r"services", ServiceViewSet, basename="service")


#paymentUser_router = DefaultRouter()
pagos_v2_router.register(r"payments", PaymentUserViewSet, basename="paymentUser")


#ExpiredPayment_router = DefaultRouter()
pagos_v2_router.register(r"expired-payments", ExpiredPaymentViewSet, basename="expired-payments")


urlpatterns = pagos_v2_router.urls

# urlpatterns += paymentUser_router.urls
# urlpatterns += ExpiredPayment_router.urls