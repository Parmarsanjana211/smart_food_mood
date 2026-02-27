from django.db import migrations, models

class FoodItem(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('romantic', 'Romantic'),
    ]
    
    name = models.CharField(max_length=100)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    image_url = models.URLField(blank=True) # Yahan hum internet se photo ka link daal sakte hain
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.mood})"