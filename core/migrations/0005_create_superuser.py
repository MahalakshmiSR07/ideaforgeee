from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='admin@example.com',
            password=make_password('admin123'),
            is_superuser=True,
            is_staff=True
        )

def remove_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='admin').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_load_projects_fixture'),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_code=remove_superuser),
    ]
