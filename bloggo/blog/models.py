from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Entry(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('bloggo.blog.views.entry_detail', args=[str(self.id)])
