from django.contrib import admin
from .models import *
# Register your models here.
from .models import MedicineDetails

admin.site.register(MedicineDetails)

from .models import ExpiredMedicineList

admin.site.register(ExpiredMedicineList)

from .models import BillingDetails

admin.site.register(BillingDetails)

from .models import PurchaseDetails

admin.site.register(PurchaseDetails)

from .models import RequiredMedicineList

admin.site.register(RequiredMedicineList)

from .models import Customer
admin.site.register(Customer)



from .models import FinancialReports

admin.site.register(FinancialReports)

from django.contrib.auth.models import Group
admin.site.unregister(Group)
admin.site.site_header = 'Pharmacy Administration Dashboard'

admin.site.register(Order)
admin.site.register(OrderItem)

