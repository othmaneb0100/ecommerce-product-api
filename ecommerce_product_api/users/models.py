from django.contrib.auth.models import User
from django.db import models

# If you want to extend the User model, you can create a profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want for the user profile
