# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now_add=True)),
                ('delete', models.SmallIntegerField(verbose_name='是否删除', default=False)),
                ('image', models.ImageField(verbose_name='图片', upload_to='goods')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
                'db_table': 'df_goods_image',
            },
        ),
        migrations.RenameModel(
            old_name='GoodCategory',
            new_name='GoodsCategory',
        ),
        migrations.RenameModel(
            old_name='GoodSKU',
            new_name='GoodsSKU',
        ),
        migrations.RenameModel(
            old_name='GoodSPU',
            new_name='GoodsSPU',
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU'),
        ),
    ]
