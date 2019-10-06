from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model
# Create your models here.

import misaka

User = get_user_model()

class Post(models.Model):
    user = models.models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.models.models.models.DateTimeField(auto_now=True)
    message = models.models.TextField()
    message_html = models.models.TextField(editable = False)
    group = models.models.ForeignKey(Group, null = True,blank = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
    
    def save(self,*args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post:single', kwargs={"username": self.user.username,'pk':self.pk})
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']