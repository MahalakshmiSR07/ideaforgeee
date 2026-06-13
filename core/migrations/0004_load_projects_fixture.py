from django.db import migrations
from django.core.management import call_command

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'projects.json', app_label='core')

def unload_fixture(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    Project.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_project_id_alter_savedproject_id_and_more'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
