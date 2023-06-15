from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics


class CompanyList(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

class CommentList(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class CommentListByCompany(generics.ListAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return models.Comment.objects.filter(company=company_id)
    
# Create your views here.
