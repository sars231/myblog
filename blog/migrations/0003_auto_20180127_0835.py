# Generated by Django 2.0 on 2018-01-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180114_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, help_text='可选项，若为空格则摘取正文前54个字符', max_length=54, null=True, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', '草稿'), ('p', '发表')], max_length=1, verbose_name='文章状态'),
        ),
    ]
