from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'applications'

class Application(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    interview_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.position

    class Meta:
        app_label = 'applications'
