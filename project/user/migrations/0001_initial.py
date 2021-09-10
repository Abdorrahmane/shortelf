# Generated by Django 3.2.7 on 2021-09-10 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=30)),
                ('paypal_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_activity_at', models.DateTimeField(auto_now_add=True)),
                ('activity_type', models.IntegerField(choices=[(0, 'Loged In'), (1, 'Loged Out'), (2, 'Changed Password'), (3, 'Changed Phone Number')])),
                ('ip_address', models.GenericIPAddressField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Withdraw'), (2, 'Dispute')])),
                ('status', models.IntegerField(choices=[(0, 'In Progress'), (1, 'Approved'), (2, 'Rejected')])),
                ('made_at', models.DateTimeField(auto_now_add=True)),
                ('last_modification_at', models.DateTimeField(auto_now=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
    ]
