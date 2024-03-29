from django.db import models

# Create your models here.
from django.utils import timezone

class LogMessage(models.Model):
    name = models.CharField(max_length=300)
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.name} said {self.message}' on {date.strftime('%A, %d %B, %Y at %X')}"
