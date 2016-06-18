from rest_framework import serializers
from models import WorkerList, Worker, Funds, FundsTicket, Costs, CostsTicket

class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerList
        fields = ('id', 'name')

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            'id',
            'name',
            'surname',
            'status',
            'pay',
            'workerlist',
        )
class CostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costs
        fields = ('id', 'name', 'money')

class CostsTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostsTicket
        fields = ('id', 'name', 'money', 'costs')    

class FundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funds
        fields = ('id', 'name', 'money')

class FundsTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundsTicket
        fields = ('id', 'name', 'money', 'funds') 