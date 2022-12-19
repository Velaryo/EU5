from .models import Service, Payment_user, Expired_payment
from .serializers import ServiceSerializer, PaymentUserSerializer, ExpiredPaymentSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.db.models import F
import random
from rest_framework import filters
from rest_framework.throttling import UserRateThrottle

class ServiceViewSet(ModelViewSet):
	queryset = Service.objects.all().order_by('-id')
	serializer_class = ServiceSerializer
	throttle_classes = [UserRateThrottle]

	ADMIN_ACTIONS = ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']
	USER_ACTIONS = ['list', 'retrieve']

	def get_permissions(self):
		permissions_classes = []
		if self.action in self.USER_ACTIONS:
			permissions_classes = [IsAuthenticated]
		elif self.action in self.ADMIN_ACTIONS:
			permissions_classes = [IsAdminUser]
		
		return [permission() for permission in permissions_classes]

class PaymentUserViewSet(ModelViewSet):
	queryset = Payment_user.objects.all().order_by('-id')
	serializer_class = PaymentUserSerializer
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['paymentDate', 'expirationDate']
	search_fields = ['paymentDate', 'expirationDate']
	throttle_scope = 'pagos'

	ADMIN_ACTIONS = ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']
	USER_ACTIONS = ['list', 'retrieve', 'create']

	"""Verifica que la fecha de exp no sea superior al de pago.
	Si lo es, lo agrega a la tabla `expired_payments`"""
	def __init__(self, *args, **kwargs):	
		res = Payment_user.objects.filter(paymentDate__gt=F('expirationDate'))
		for x in res:
			obj, created = Expired_payment.objects.get_or_create(pay_user=x)
			#si fue creado, actualiza el campo penalty del obj x un valor random
			if created:
				obj.penalty_fee_amount = random.randint(10,50)
				obj.save()
	
	def get_permissions(self):
		permissions_classes = []
		if self.action in self.USER_ACTIONS:
			permissions_classes = [IsAuthenticated]
		elif self.action in self.ADMIN_ACTIONS:
			permissions_classes = [IsAdminUser]
		
		return [permission() for permission in permissions_classes]

class ExpiredPaymentViewSet(ModelViewSet):
	queryset = Expired_payment.objects.all().order_by('-id')
	serializer_class = ExpiredPaymentSerializer
	throttle_classes = [UserRateThrottle]
	

	ADMIN_ACTIONS = ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']
	USER_ACTIONS = ['list', 'retrieve', 'create']

	def get_permissions(self):
		permissions_classes = []
		if self.action in self.USER_ACTIONS:
			permissions_classes = [IsAuthenticated]
		elif self.action in self.ADMIN_ACTIONS:
			permissions_classes = [IsAdminUser]
		
		return [permission() for permission in permissions_classes]
	

		
	
