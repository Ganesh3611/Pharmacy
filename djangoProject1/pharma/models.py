# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('T', 'Tablets'),
    ('S', 'Syrup'),
    ('V', 'Vitamins'))


class BillingDetails(models.Model):
    billing_id = models.BigIntegerField(primary_key=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    customer_address = models.CharField(max_length=50, blank=True, null=True)
    medicine_list = models.CharField(max_length=100, blank=True, null=True)
    billing_date = models.DateField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'billing_details'


class ExpiredMedicineList(models.Model):
    expired_id = models.BigIntegerField(primary_key=True)
    medicine_name = models.ForeignKey('MedicineDetails', models.DO_NOTHING, db_column='medicine_name', blank=True,
                                      null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    store_box = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'expired_medicine_list'


class FinancialReports(models.Model):
    financial_id = models.BigIntegerField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    total_credit = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    total_debit = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    profit_loss_status = models.CharField(max_length=20, blank=True, null=True)
    value = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'financial_reports'


class MedicineDetails(models.Model):
    medicine_id = models.BigIntegerField(primary_key=True)
    medicine_image = models.ImageField(upload_to='Pictures')
    medicine_name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, blank=True, null=True)
    store_box = models.CharField(max_length=20, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    selling_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    generic_name = models.CharField(max_length=20, blank=True, null=True)
    side_effects = models.CharField(max_length=20, blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    offer = models.BooleanField()
    slug = models.SlugField()

    class Meta:
        managed = True
        db_table = 'medicine_details'

    def get_absolute_url(self):
        return reverse("pharma:shop-single", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("pharma:add-to-cart", kwargs={
            'slug': self.slug
        })


class OrderDetails(models.Model):
    item = models.ForeignKey(MedicineDetails, db_column='medicine_name', on_delete=models.CASCADE)
    order_date = models.DateField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    customer_address = models.CharField(max_length=50, blank=True, null=True)
    medicine_list = models.CharField(max_length=50, blank=True, null=True)
    payment_mode = models.CharField(max_length=20, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_details'

    def __str__(self):
        return f"{self.item.quantity} of {self.item.medicine_id}"


class PurchaseDetails(models.Model):
    purchase_id = models.BigIntegerField(primary_key=True)
    medicine_name = models.ForeignKey(MedicineDetails, models.DO_NOTHING, db_column='medicine_name',
                                      related_name='medicines_id', blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    purchase_quantity = models.FloatField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'purchase_details'


class RequiredMedicineList(models.Model):
    required_id = models.BigIntegerField(primary_key=True)
    medicines_id = models.ForeignKey(MedicineDetails, models.DO_NOTHING, db_column='medicines_id', blank=True,
                                     null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    required_quantity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'required_medicine_list'


from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(MedicineDetails, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address
