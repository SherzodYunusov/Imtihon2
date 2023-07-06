# Generated by Django 4.2.1 on 2023-07-06 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('yosh', models.IntegerField()),
                ('ish_vaqt', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Haydovchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.IntegerField()),
                ('kiritilgan_sana', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=50)),
                ('narx', models.IntegerField()),
                ('litr', models.CharField(max_length=100)),
                ('batafsil', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.IntegerField()),
                ('manzil', models.CharField(max_length=50)),
                ('qarz', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.CharField(max_length=50)),
                ('umumiy_summa', models.IntegerField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.admin')),
                ('haydovchi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.haydovchi')),
                ('mijoz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mijoz')),
                ('suv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.suv')),
            ],
        ),
    ]
