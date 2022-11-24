from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16,unique=True)
    description = models.TextField(blank=True)
    # Основные типы полей
    # Дата
    # Числа
    # Логические
    # Байты
    # Картинка
    # Файл
    # url, email
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=32,unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Связь с категорией
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # Связь с тегами
    tag = models.ManyToManyField(Tag)


