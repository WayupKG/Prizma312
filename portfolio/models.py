
from django.db.models import *
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


def upload_to_title_img(instance, filename):
    list_file = filename.split('.')
    return '%s/Portfolio/%s/img/%s/' % (instance.user.username, f'{instance.title}',
                                        f'{instance.user.username}-{instance.title}.{list_file[-1]}')


def upload_to_portfolio(instance, filename):
    list_file = filename.split('.')
    return '%s/Portfolio/%s/%s/' % (instance.user.username, f'{instance.title}',
                                    f'{instance.user.username}-{instance.title}.{list_file[-1]}')


class Category(Model):
    name = CharField('Название', max_length=150, db_index=True)
    slug = SlugField(max_length=200)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Portfolio(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='portfolio')
    title = CharField('Название', max_length=200)
    slug = SlugField(max_length=250)
    body = RichTextField('Описание')
    category = ForeignKey(Category, on_delete=CASCADE, related_name='portfolio', null=True)
    tags = TaggableManager()
    img = ImageField(upload_to=upload_to_title_img)
    zip_file = FileField(upload_to=upload_to_portfolio)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
