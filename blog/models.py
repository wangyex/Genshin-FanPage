from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length = 100)
    header_image = models.ImageField(null=True, blank = True, upload_to = "images/")
    description = models.TextField()
    body = RichTextField(blank = True, null = True)
    date = models.DateField()

    def __str__(self):
        return self.title