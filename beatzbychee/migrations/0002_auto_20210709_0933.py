# Generated by Django 3.2.5 on 2021-07-09 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beatzbychee', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message_Topic',
            new_name='MessageTopic',
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('message_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beatzbychee.messagetopic')),
            ],
            options={
                'verbose_name_plural': 'messages',
            },
        ),
    ]
