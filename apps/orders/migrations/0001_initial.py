# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_address'),
        ('goods', '0004_indexpromotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True, null=True)),
                ('delete', models.SmallIntegerField(default=False, verbose_name='是否删除')),
                ('count', models.IntegerField(default=1, verbose_name='购买数量')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='单价', max_digits=10)),
                ('comment', tinymce.models.HTMLField(default='', verbose_name='评价信息')),
            ],
            options={
                'db_table': 'df_order_goods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True, null=True)),
                ('delete', models.SmallIntegerField(default=False, verbose_name='是否删除')),
                ('order_id', models.CharField(verbose_name='订单号', max_length=64, primary_key=True, serialize=False)),
                ('total_count', models.IntegerField(default=1, verbose_name='商品总数')),
                ('total_amount', models.DecimalField(decimal_places=2, verbose_name='商品总金额', max_digits=10)),
                ('trans_cost', models.DecimalField(decimal_places=2, verbose_name='运费', max_digits=10)),
                ('pay_method', models.SmallIntegerField(default=1, verbose_name='支付方式', choices=[(1, '货到付款'), (2, '微信支付'), (3, '支付宝'), (4, '银联支付')])),
                ('status', models.SmallIntegerField(default=1, verbose_name='订单状态', choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')])),
                ('trade_no', models.CharField(default='', verbose_name='支付编号', max_length=100, unique=True, blank=True, null=True)),
                ('address', models.ForeignKey(verbose_name='收货地址', to='users.Address')),
                ('user', models.ForeignKey(verbose_name='下单用户', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'df_order_info',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(verbose_name='所属订单', to='orders.OrderInfo'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='sku',
            field=models.ForeignKey(verbose_name='订单商品', to='goods.GoodsSKU'),
        ),
    ]
