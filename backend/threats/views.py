from django.shortcuts import render

# Create your views here.
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CyberAttack

@api_view(['GET'])
def top_countries(request):
    data = (
        CyberAttack.objects
        .values('country')
        .annotate(count=Count('id'))
        .order_by('-count')[:10]
    )
    return Response(data)

@api_view(['GET'])
def top_years(request):
    data = (
        CyberAttack.objects
        .values('year')
        .annotate(count=Count('id'))
        .order_by('-count')
    )
    return Response(data)

@api_view(['GET'])
def top_threat_types(request):
    data = (
        CyberAttack.objects
        .values('attack_type')
        .annotate(count=Count('id'))
        .order_by('-count')
    )
    return Response(data)

@api_view(['GET'])
def top_industries(request):
    data = (
        CyberAttack.objects
        .values('target_industry')
        .annotate(count=Count('id'))
        .order_by('-count')
    )
    return Response(data)
