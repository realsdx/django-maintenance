from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class MainteneceMode(models.Model):
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if MainteneceMode.objects.exists() and not self.pk:
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one MainteneceMode instance')
        return super(MainteneceMode, self).save(*args, **kwargs)