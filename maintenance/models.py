from django.db import models

# Create your models here.
class MainteneceMode(models.Model):
    status = models.BooleanField(default=False)