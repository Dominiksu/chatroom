from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse 

User = get_user_model()

class Chatroom(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,)
    desc = models.TextField(max_length= 500, blank= True)
    image = models.ImageField(blank = True, null = True, upload_to='room/')



    def __str__(self):
        return self.name
    
    def user_name(self):
        if self.created_by:
            return self.created_by.username
    
    def get_absolute_url(self):
        return reverse("Chatroom_detail", kwargs={"pk": self.pk})
    

    def get_absolute_url_delete(self):
        return reverse("Chatroom_delete", kwargs={"pk": self.pk})
    



class Messages(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(Chatroom, on_delete = models.CASCADE)
    create_dt = models.DateTimeField(auto_now= True)
    content = models.TextField(max_length = 350)

