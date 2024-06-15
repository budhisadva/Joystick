from django.shortcuts import render, redirect
import serial

def index(request):
    return render(request, 'index.html')
