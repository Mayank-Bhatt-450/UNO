from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class rooms(models.Model):
    name=models.CharField(max_length=100)
    host=models.CharField(max_length=100)
    gamestart=models.CharField(max_length=6,default=False)

class Userinfo(models.Model):
    user =  models.OneToOneField(User)
    room=models.OneToManyField(rooms,related_name='players',default=None))
    #status = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.username
class player_game_state(models.Model):
    turn=models.CharField(max_length=6,default=False)
    hand_cards=models.CharField(max_length=800,default='')
    guno=models.CharField(max_length=6,default=False)
class game_state(models.Model):
    current=models.CharField(max_length=30,default="['','']")
    num_deck_card=models.IntegerField()
    draw_break=models.CharField(max_length=6,default=False)
    turn_flag=models.CharField(max_length=6,default=False)
    pile=models.IntegerField()
    num_of_players=models.IntegerField()
class game_state_op(models.Model):
    current=models.CharField(max_length=1500,default="['','']")
