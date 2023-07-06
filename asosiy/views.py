from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import *
from .serializer import *

class SuvApiView(APIView):
    def get(self, request):
        suv = Suv.objects.all()
        serializer = SuvSerializer(suv, many=True)
        return Response(serializer.data)

class MijozApiView(APIView):
    def get(self, request):
        mijoz = Mijoz.objects.all()
        serializer = SuvSerializer(mijoz, many=True)
        return Response(serializer.data)

# class BuyurtmaApiView(APIView):
#     def get(self, request):
#         buyurtma = Buyurtma

class AdminApiView(APIView):
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        a = AdminSerizlizer(admin)
        return Response(a.data)

class HaydovchiApiView(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        h = HaydovchiSerializer(haydovchi)
        return Response(h.data)

class BuyurtmaApiView(APIView):
    def get(self, request):
        buyurtma = Buyurtma.objects.all()
        b = BuyurtmaSerializer(buyurtma, many=True)
        return Response(b.data)

    def post(self, request):
        malumot = request.data
        serializer = BuyurtmaSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSeriazlizer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism', 'tel']
    ordering_fields = ['qarz']

class SuvModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brend']
    ordering_fields = ['narx']

# Create your views here.
