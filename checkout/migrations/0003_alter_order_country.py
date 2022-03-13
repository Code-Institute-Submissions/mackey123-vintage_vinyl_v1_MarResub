""" checkout for different country types """
from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):
    """checkout dependencies for different countries"""

    dependencies = [
        ('checkout', '0002_auto_20220204_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
