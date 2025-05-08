from django.db import models

# Model representing product categories (e.g., Electronics, Clothing)    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name