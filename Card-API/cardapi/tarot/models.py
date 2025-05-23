from django.db import models

class ReadingSubmission(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
