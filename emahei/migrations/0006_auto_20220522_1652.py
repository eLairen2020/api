# Generated by Django 3.2 on 2022-05-22 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emahei', '0005_auto_20220522_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_enroll_details',
            name='date_of_purchase',
        ),
        migrations.AddField(
            model_name='course_enroll_details',
            name='date_of_enroll',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='enotes',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.school'),
        ),
        migrations.AddField(
            model_name='enotes',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emahei.standard'),
        ),
        migrations.AddField(
            model_name='enotes',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emahei.subject'),
        ),
        migrations.AddField(
            model_name='enotes',
            name='upload',
            field=models.FileField(default=0, upload_to='doc/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liveclass', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emahei.liveclass')),
                ('student_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ManyToManyField(blank=True, related_name='classtakingteacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]