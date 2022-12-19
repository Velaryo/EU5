from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import random

class Service(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	logo = models.URLField()

	class Meta:
		db_table = 'services'

	def __str__(self):
		return self.name

class Payment_user(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_users')
	service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='payment_services')
	amount = models.FloatField(default=0.0)
	paymentDate = models.DateField(default="")
	expirationDate = models.DateField()

	class Meta:
		db_table = 'payment_user'

	def __str__(self):
		texto = f"{self.id}| {self.user} ({self.service})"

		if self.paymentDate > self.expirationDate:
			return f"{texto} - CADUCADO" 

		return f"{texto} - Vigente"

class Expired_payment(models.Model):
	pay_user = models.ForeignKey(Payment_user, on_delete=models.CASCADE, related_name='expired_payments')
	penalty_fee_amount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(50)], default=0.0)
	
	class Meta:
		db_table = 'expired_payments'