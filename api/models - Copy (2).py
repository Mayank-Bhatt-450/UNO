from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
{"current": ["", ""], "num_deck_card": 0, "draw_break": True, "turn_flag": 0, "pile": 0, "num_of_players": 0,
"0": {"turn": "false", "guno": True, "name": "name", "hand_cards": [["red", "o"]]},
"1": {"turn": "true", "guno": False, "name": "name", "hand_cards": [["red", "0"], ["yellow", "8"]]}}

"""
class rooms(models.Model):
    name=models.CharField(max_length=100)
    host=models.CharField(max_length=100,primary_key=True)
    gamestart= models.BooleanField(default=False)
    #gamestate= models.OneToOneField(game_state_op,on_delete=models.CASCADE)
    global_variabl=models.CharField(max_length=3000,default=
    '{"current": ["", ""], "deck": [["red", "0"], ["red", "1"], ["red", "2"], ["red", "3"], ["red", "4"], ["red", "5"], ["red", "6"], ["red", "7"], ["red", "8"], ["red", "9"], ["red", "o"], ["red", "r"], ["red", "+2"], ["yellow", "0"], ["yellow", "1"], ["yellow", "2"], ["yellow", "3"], ["yellow", "4"], ["yellow", "5"], ["yellow", "6"], ["yellow", "7"], ["yellow", "8"], ["yellow", "9"], ["yellow", "o"], ["yellow", "r"], ["yellow", "+2"], ["green", "0"], ["green", "1"], ["green", "2"], ["green", "3"], ["green", "4"], ["green", "5"], ["green", "6"], ["green", "7"], ["green", "8"], ["green", "9"], ["green", "o"], ["green", "r"], ["green", "+2"], ["blue", "0"], ["blue", "1"], ["blue", "2"], ["blue", "3"], ["blue", "4"], ["blue", "5"], ["blue", "6"], ["blue", "7"], ["blue", "8"], ["blue", "9"], ["blue", "o"], ["blue", "r"], ["blue", "+2"], ["black", "+4"], ["black", "+4"], ["black", "c"], ["black", "c"]], "shuffel_deck": [], "pile": 0, "turn": 0, "turn_num": 0, "turnflag": 0, "pt": 0}')
class game_state_op(models.Model):
    room= models.OneToOneField(rooms,related_name='gamestate',on_delete=models.CASCADE)
    game_state_db=models.CharField(max_length=1500,default=
    '{"current": ["", ""], "num_deck_card": 0, "draw_break": true, "turn_flag": 0, "pile": 0, "num_of_players": 0}')


class Userinfo(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    room=models.ForeignKey(rooms,on_delete=models.SET_NULL,related_name="players", blank=True, null=True)
    #status = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.username
class player_game_state(models.Model):
    turn=models.CharField(max_length=6,default=False)
    hand_cards=models.CharField(max_length=800,default="")
    guno=models.CharField(max_length=6,default=False)
class game_state(models.Model):
    current=models.CharField(max_length=30,default="['','']")
    num_deck_card=models.IntegerField()
    draw_break=models.CharField(max_length=6,default=False)
    turn_flag=models.CharField(max_length=6,default=False)
    pile=models.IntegerField()
    num_of_players=models.IntegerField()
