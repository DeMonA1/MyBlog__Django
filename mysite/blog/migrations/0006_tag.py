# Generated by Django 5.1.1 on 2024-10-13 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_triagram_ext'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('taggit.tag',),
        ),
    ]