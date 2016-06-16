from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import WorkerListSerializer, WorkerSerializer, FundsSerializer, FundsTicketSerializer, CostsSerializer, CostsTicketSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .models import Worker, WorkerList, Funds ,FundsTicket, Costs, CostsTicket


class WorkerListViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerListSerializer
    queryset = serializer_class.Meta.model.objects.all()
    
    @detail_route(methods=['get'])
    def ListAllWorkers(self, request, pk):
        workerlist = self.get_object()
        worker = Worker.objects.all().filter(workerlist=pk)
        serializer = WorkerSerializer(worker, context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def ListActiveWorkers(self, request, pk):
        WorkerList = self.get_object()
        worker = Worker.objects.all().filter(workerlist=pk, status='Active')
        serializer = WorkerSerializer(worker, context={'request': request}, many=True)
        return Response(serializer.data)

class WorkerViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = serializer_class.Meta.model.objects.all()

class FundsViewSet(viewsets.ModelViewSet):
    serializer_class = FundsSerializer
    queryset = serializer_class.Meta.model.objects.all()

    @detail_route(methods=['get'])
    def ListAllFunds(self, request, pk):
        fund = self.get_object()
        fundticket = FundsTicket.objects.all().filter(funds_id=pk)
        serializer = FundsSerializer(fundticket, context={'request': request}, many=True)
        return Response(serializer.data)

   #def ListFundsByMoney(self ,request ,pk=None)

class FundsTicketViewSet(viewsets.ModelViewSet):
    serializer_class = FundsTicketSerializer
    queryset = serializer_class.Meta.model.objects.all()

    #def UpdateFundTicket()

    #def DeleteFundTicket(self ,request ,pk=None):

    #def GetFundTicket()

class CostsViewSet(viewsets.ModelViewSet):
    serializer_class = CostsSerializer
    queryset = serializer_class.Meta.model.objects.all()

    @detail_route(methods=['get'])
    def ListAllCosts(self, request, pk):
        cost = self.get_object()
        costticket = CostsTicket.objects.all().filter(costs_id=pk)
        serializer = CostsSerializer(costticket, context={'request': request}, many=True)
        return Response(serializer.data)

    #def ListCostsByMoney()

class CostsTicketViewSet(viewsets.ModelViewSet):
    serializer_class = CostsTicketSerializer
    queryset = serializer_class.Meta.model.objects.all()

    #def UpdateCost()

    #def DeleteFund()

    #def GetFund()