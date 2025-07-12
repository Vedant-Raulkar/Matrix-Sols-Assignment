from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Collage(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    template_id = models.CharField(max_length=50, default='template_2_1')
    frame_style = models.CharField(max_length=20, choices=[
        ('modern', 'Modern'),
        ('classic', 'Classic'),
        ('minimal', 'Minimal'),
        ('vintage', 'Vintage'),
    ], default='modern')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('collages:detail', kwargs={'pk': self.pk})
    
    @property
    def image_count(self):
        return self.images.count()


class ImageItem(models.Model):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='collages/%Y/%m/%d/')
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    # Position coordinates for freeform layout
    x_position = models.FloatField(default=0)
    y_position = models.FloatField(default=0)
    width = models.FloatField(default=200)
    height = models.FloatField(default=200)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Image {self.order} in {self.collage.title}"
