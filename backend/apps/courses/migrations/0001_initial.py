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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('target_audience', models.CharField(blank=True, max_length=255)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('difficulty', models.CharField(choices=[('básico', 'Básico'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')], default='básico', max_length=50)),
                ('category', models.CharField(blank=True, help_text='Ej: Matemáticas, Quechua, Educación Cívica', max_length=100)),
                ('language', models.CharField(default='Español', max_length=50)),
                ('estimated_duration', models.PositiveIntegerField(blank=True, help_text='Duración estimada en minutos', null=True)),
                ('xp_reward', models.PositiveIntegerField(default=100, help_text='Puntos XP otorgados al completar el curso')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
