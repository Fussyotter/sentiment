from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    text = models.TextField()
    sentiment_score = models.FloatField()