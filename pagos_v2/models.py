from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Service(models.Model):
	name = models.CharField(max_length="50")
	description = models.TextField()
	logo = models.URLField()

	class Meta:
		db_table = 'services'

class Payment_user(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
	service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
	amount = models.FloatField(default=0.0)
	paymentDate = models.DateField(default="")
	expirationDate = models.DateField()

	class Meta:
		db_table = 'payment_user'

class Expired_payments(models.Model):
	pay_user_id = models.ForeignKey(Payment_user, on_delete=models.CASCADE, related_name='payment_users')
	penalty_fee_amount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(50)])
	