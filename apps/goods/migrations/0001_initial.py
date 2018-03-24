# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now_add=True)),
                ('delete', models.SmallIntegerField(verbose_name='是否删除', default=False)),
                ('name', models.CharField(max_length=20, verbose_name='类别名称')),
                ('logo', models.CharField(max_length=100, verbose_name='图标标识')),
                ('image', models.ImageField(upload_to='category', verbose_name='类别名称')),
            ],
            options={
                'verbose_name': '商品类别',
                'db_table': 'df_good_category',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.CreateModel(
            name='GoodSKU',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now_add=True)),
                ('delete', models.SmallIntegerField(verbose_name='是否删除', default=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('title', models.CharField(max_length=200, verbose_name='简介')),
                ('unit', models.CharField(max_length=10, verbose_name='销售单位')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='价格', max_digits=10)),
                ('stock', models.IntegerField(verbose_name='库存', default=0)),
                ('sales', models.IntegerField(verbose_name='销售', default=0)),
                ('default_image', models.ImageField(upload_to='goods', verbose_name='图片')),
                ('status', models.BooleanField(verbose_name='是否上线', default=True)),
                ('category', models.ForeignKey(to='goods.GoodCategory', verbose_name='类别')),
            ],
            options={
                'verbose_name': '商品SKU',
                'db_table': 'df_goods_sku',
                'verbose_name_plural': '商品SKU',
            },
        ),
        migrations.CreateModel(
            name='GoodSPU',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', null=True, auto_now_add=True)),
                ('delete', models.SmallIntegerField(verbose_name='是否删除', default=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('desc', tinymce.models.HTMLField(verbose_name='商品描述', blank=True, default='')),
            ],
            options={
                'verbose_name': '商品',
                'db_table': 'df_goods_spu',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.AddField(
            model_name='goodsku',
            name='spu',
            field=models.ForeignKey(to='goods.GoodSPU', verbose_name='商品SPU'),
        ),
    ]
