# Generated by Django 3.1.5 on 2021-01-27 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20210102_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='models.basemodel')),
            ],
            bases=('models.basemodel',),
        ),
        migrations.CreateModel(
            name='TeacherPermissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': [('can_manage_team_permissions', 'Can Manage Team Permissions')],
            },
        ),
    ]
