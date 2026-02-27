import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from blog.models import Post

print('count', Post.objects.count())
print('published', Post.objects.filter(published=True).count())
