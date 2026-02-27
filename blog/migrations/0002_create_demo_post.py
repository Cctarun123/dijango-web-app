from django.db import migrations
from django.conf import settings


def create_demo_post(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    User = apps.get_model(settings.AUTH_USER_MODEL.split('.')[0], settings.AUTH_USER_MODEL.split('.')[1])
    # ensure there's at least one user
    user, created = User.objects.get_or_create(username='demo', defaults={'password':'', 'is_staff':False})
    if not Post.objects.filter(title='Welcome to the blog').exists():
        Post.objects.create(
            title='Welcome to the blog',
            content='This is your first post. Edit or delete it, then start blogging!',
            author=user,
            published=True,
        )


def reverse_func(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(title='Welcome to the blog').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_demo_post, reverse_func),
    ]
