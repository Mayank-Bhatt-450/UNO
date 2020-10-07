from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Userinfo)
admin.site.register(models.rooms)
admin.site.register(models.player_game_state)
admin.site.register(models.game_state)
admin.site.register(models.game_state_op)
