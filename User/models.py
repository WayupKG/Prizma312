from django.db.models import *
from django.contrib.auth.models import User


def upload_to_user(instance, filename):
    return '%s/%s/%s/' % (instance.user.username, 'Avatar', f'{instance.user.username}-{filename}.png')


class UserInfo(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='info')
    avatar = ImageField(upload_to=upload_to_user)
    profession = CharField('Профессия', max_length=150)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'
