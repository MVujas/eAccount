from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'WorkerList', views.WorkerListViewSet)
router.register(r'Worker', views.WorkerViewSet)
router.register(r'Funds', views.FundsViewSet)
router.register(r'FundsTicket', views.FundsTicketViewSet)
router.register(r'Costs', views.CostsViewSet)
router.register(r'CostsTicket', views.CostsTicketViewSet)

urlpatterns = patterns(
    '',
    url(
            r'^v0/',
                include(
                            router.urls,
                        ),
            ),
        );
