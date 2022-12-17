from django.db import models
from users.models import User

class Pago(models.Model):

	SERVICIOS_CHOICES = (
        ('n', 'Netflix'),
        ('a', 'Amazon Video'),
        ('s', 'Star +'),
		('p', 'Paramount +')
    )

	servicio = models.CharField(max_length=1, choices=SERVICIOS_CHOICES)
	monto = models.FloatField(default=0)
	fecha = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

	class Meta:
		db_table = 'pagos'