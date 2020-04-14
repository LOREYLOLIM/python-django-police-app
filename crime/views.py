from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Report
from .forms import ReportForm

# Create your views here.

def home(request):
    template = 'index.html'
    return render(request, template)

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReportForm
    template = 'report.html'
    context = {'form':form}
    return render(request,template, context)

def police(request):
    reports = Report.objects.all()
    context = {'reports':reports}
    template = 'police.html'
    return render(request,template, context)

def delete(request, id):
    police = get_object_or_404(Report, id=id)
    police.delete()
    return redirect('police')

   

