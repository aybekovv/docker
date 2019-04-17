from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    coins = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    remain_coins = models.IntegerField(default=100)

    def __str__(self):
        return str(self.user.username)

    def adding_coins_to_profile(self, coins_from_input):
        self.coins = self.coins + coins_from_input
        return self.coins

    def profile_level_up(self, coins_from_input):
        self.adding_coins_to_profile(coins_from_input)

        user_coins = self.coins
        level = 1
        need_coins = 100
        remain_coins = self.remain_coins

        while user_coins > 0:
            if user_coins >= need_coins:
                user_coins -= need_coins
                level += 1
                need_coins += 50
                if user_coins < need_coins:
                    remain_coins = need_coins - user_coins
                    break
            else:
                remain_coins = need_coins - user_coins
                break
        self.remain_coins = remain_coins
        self.level = level
        return self.level


    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
