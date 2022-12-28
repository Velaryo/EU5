from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

def create_jwt_pair_for_user(user: User):
    refresh = RefreshToken.for_user(user)

    tokens = {
    	"id": str(user.id),
		"first_name": str(user.first_name),
		"is_staff": str(user.is_staff),
		"is_superuser": str(user.is_superuser),
		"is_active": str(user.is_active),
		"access": str(refresh.access_token), 
		"refresh": str(refresh)
		}

    return tokens

	