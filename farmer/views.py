from django.shortcuts import render
from django.http import HttpResponse
from .forms import FarmerForm
from .models import Resume
from django.views import View

# Create your views here.
class HomeView(View):
 def get(self, request):
  form = FarmerForm()
  candidates = Resume.objects.all()
  return render(request, 'total/farm.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = FarmerForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'total/farm.html', {'form':form})


class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'total/output.html', {'candidate':candidate})