from .models import Pago
from .serializers import PagoSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import mixins


# class IsAuthenticated(permissions.BasePermission):
#     def has_permission(self, request, view):
#     	return request.user and request.user.is_authenticated

class PagoCreateRetrieveUpdateListViewSet(mixins.CreateModelMixin,\
	mixins.RetrieveModelMixin, mixins.UpdateModelMixin, \
		mixins.ListModelMixin, GenericViewSet):
	
	#actions = ['list', 'create', 'retrieve', 'update', 'partial_update']

	#permission_classes = [IsAuthenticated]
	queryset = Pago.objects.all().order_by('-id')
	serializer_class = PagoSerializer

	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['servicio','fecha', 'user']

	def get_throttles(self):
		if self.action == "create":
			
			self.throttle_scope = "create"
		return super().get_throttles()

