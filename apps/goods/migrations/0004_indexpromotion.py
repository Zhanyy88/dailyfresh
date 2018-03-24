# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_indexcategorygoods_indexslidegoods'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(null=True, auto_now_add=True, verbose_name='更新时间')),
                ('delete', models.SmallIntegerField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=50, verbose_name='活动名称')),
                ('url', models.CharField(max_length=100, verbose_name='活动链接')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
            ],
            options={
                'db_table': 'df_index_promotion',
                'verbose_name_plural': '主页活动促销',
                'verbose_name': '主页活动促销',
            },
        ),
    ]
