# Generated by Django 3.0.4 on 2020-05-26 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0014_auto_20200526_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name',), 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='name',
        ),
    ]
