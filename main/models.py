from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

# TARGET_CHOICES = [
#     ("men", "Men"),
#     ("women", "Women"),
#     ("kids", "Kids"),
# ]
# title = models.CharField(choices=TARGET_CHOICES)


# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    about = models.TextField(blank=True, null=True, validators=[
                             MaxLengthValidator(2000)])
    image = models.ImageField(blank=True, null=True,
                              upload_to="profile-images")

    def __str__(self):
        return f"{self.user}"
