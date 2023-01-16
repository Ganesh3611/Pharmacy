# Generated by Django 3.2.2 on 2021-05-17 15:00

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
            name='BillingDetails',
            fields=[
                ('billing_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=50, null=True)),
                ('medicine_list', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_date', models.DateField(blank=True, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'db_table': 'billing_details',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FinancialReports',
            fields=[
                ('financial_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('total_credit', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('total_debit', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('profit_loss_status', models.CharField(blank=True, max_length=20, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'db_table': 'financial_reports',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedicineDetails',
            fields=[
                ('medicine_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('medicine_image', models.ImageField(upload_to='Pictures')),
                ('medicine_name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('category', models.CharField(blank=True, choices=[('T', 'Tablets'), ('S', 'Syrup'), ('V', 'Vitamins')], max_length=20, null=True)),
                ('store_box', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=20, null=True)),
                ('generic_name', models.CharField(blank=True, max_length=20, null=True)),
                ('side_effects', models.CharField(blank=True, max_length=20, null=True)),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('offer', models.BooleanField()),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'medicine_details',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RequiredMedicineList',
            fields=[
                ('required_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('company_name', models.CharField(blank=True, max_length=20, null=True)),
                ('required_quantity', models.FloatField(blank=True, null=True)),
                ('medicines_id', models.ForeignKey(blank=True, db_column='medicines_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pharma.medicinedetails')),
            ],
            options={
                'db_table': 'required_medicine_list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('purchase_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('purchase_quantity', models.FloatField(blank=True, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('medicine_name', models.ForeignKey(blank=True, db_column='medicine_name', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='medicines_id', to='pharma.medicinedetails')),
            ],
            options={
                'db_table': 'purchase_details',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=50, null=True)),
                ('medicine_list', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('order_status', models.CharField(blank=True, max_length=20, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharma.medicinedetails')),
            ],
            options={
                'db_table': 'order_details',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExpiredMedicineList',
            fields=[
                ('expired_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('store_box', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('medicine_name', models.ForeignKey(blank=True, db_column='medicine_name', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pharma.medicinedetails')),
            ],
            options={
                'db_table': 'expired_medicine_list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
