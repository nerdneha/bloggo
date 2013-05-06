from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Entry(models.Model):
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225) #, unique=True)

    def get_absolute_url(self):
        return reverse('bloggo.blog.views.view_entry', args=[str(self.id)])
