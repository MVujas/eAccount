from django.contrib import admin
from models import WorkerList, Worker, Funds, FundsTicket, Costs, CostsTicket

# Register your models here.
admin.site.register(WorkerList)
admin.site.register(Worker)
admin.site.register(Funds)
admin.site.register(FundsTicket)
admin.site.register(Costs)
admin.site.register(CostsTicket)
