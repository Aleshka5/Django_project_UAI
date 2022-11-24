from django.core.management.base import BaseCommand
from blogapp.models import Category, Post, Tag
class Command(BaseCommand):
    def handle(self,*args,**options):
        # Выбираем все категории
        categories = Category.objects.all()
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(type(item))
        print('End')