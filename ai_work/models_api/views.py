from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ModalAuthor, AIModel, ModelPurchase, UsageScenario , ModelBenchmark
from .serializers import (ModelAuthorSerializer, AIModelSerializer, ModelPurchaseSerializer,UsageScenarioSerializer, ModelBenchmarkSerializer)


# Create your views here.
class ModelAuthorViewSet(viewsets.ModelViewSet):
    queryset = ModalAuthor.objects.all()
    serializer_class = ModelAuthorSerializer

    @action(detail=True, methods=['get'])
    def models(self,request,pk=None):
        author = self.get_object()
        models = author.models_uploaded.all()
        serializer = AIModelSerializer(models, many=True)
        return Response(serializer.data)

class AIModelViewSet(viewsets.ModelViewSet):
    queryset = AIModel.objects.all()
    serializer_class = AIModelSerializer

    @action(detail=True, methods=['get'])
    def usage_scenarios(self,request,pk=None):
        model = self.get_object()
        scenarios = model.usage_scenarios.all()
        serializer = UsageScenarioSerializer(scenarios,many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def benchmark(self, request, pk=None):
        model = self.get_object()
        benchmarks = model.benchmarks.all()
        serializer = ModelBenchmarkSerializer(benchmarks,many=True)
        return Response(serializer.data)

class ModelPurchaseViewSet(viewsets.ModelViewSet):
    queryset = ModelPurchase.objects.all()
    serializer_class = ModelPurchaseSerializer

class UsageScenarioViewSet(viewsets.ModelViewSet):
    queryset = UsageScenario.objects.all()
    serializer_class = UsageScenarioSerializer

class ModelBenchmarkViewSet(viewsets.ModelViewSet):
    queryset = ModelBenchmark.objects.all()
    serializer_class = ModelBenchmarkSerializer
    