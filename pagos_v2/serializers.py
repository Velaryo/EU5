from rest_framework.serializers import ModelSerializer
from .models import Service, Payment_user, Expired_payment


class ServiceSerializer(ModelSerializer):
	class Meta:
		model = Service
		fields = ['id','name','description','logo']
		read_only_fields = ['id']

class PaymentUserSerializer(ModelSerializer):
	class Meta:
		model = Payment_user
		fields = ['id','user','service','amount', 'paymentDate', 'expirationDate']
		read_only_fields = ['id']

class ExpiredPaymentSerializer(ModelSerializer):
	class Meta:
		model = Expired_payment
		fields = ['id', 'pay_user', 'penalty_fee_amount']
		read_only_fields = ['id']
