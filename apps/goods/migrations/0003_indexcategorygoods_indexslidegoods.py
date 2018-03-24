# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180324_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexCategoryGoods',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now_add=True)),
                ('delete', models.SmallIntegerField(default=False, verbose_name='是否删除')),
                ('display_type', models.SmallIntegerField(verbose_name='展示类型', choices=[(0, '标题'), (1, '图片')])),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
                ('category', models.ForeignKey(verbose_name='商品类别', to='goods.GoodsCategory')),
                ('sku', models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU')),
            ],
            options={
                'verbose_name': '主页分类展示商品',
                'verbose_name_plural': '主页分类展示商品',
                'db_table': 'df_index_categroy_goods',
            },
        ),
        migrations.CreateModel(
            name='IndexSlideGoods',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now_add=True)),
                ('delete', models.SmallIntegerField(default=False, verbose_name='是否删除')),
                ('image', models.ImageField(verbose_name='图片', upload_to='banner')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
                ('sku', models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU')),
            ],
            options={
                'verbose_name': '主页轮播商品',
                'verbose_name_plural': '主页轮播商品',
                'db_table': 'df_index_slide_goods',
            },
        ),
    ]
