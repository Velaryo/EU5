from rest_framework.serializers import ModelSerializer
from .models import Pago

class PagoSerializer(ModelSerializer):
	class Meta:
		model = Pago
		fields = ['id','servicio','monto','user', 'fecha']
		read_only_fields = ['fecha', 'id']
		
