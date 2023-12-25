from django.shortcuts import render
from enroll.forms import ResumeForms
from django.views.generic import View
from django.contrib import messages
from enroll.models import Resume
# Create your views here.


    
class HomeView(View):
    def get(self, request):
        form = ResumeForms()
        candidates = Resume.objects.all()
        return render(request, 'enroll/home.html',{'candidates':candidates,'form':form})
    
    def post(self, request):
        form = ResumeForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Thanks Uploaded...')
            return render(request, 'enroll/home.html',{'form':form})
        
class CandidteDetailView(View):
    def get(self, request, pk):
        candidate_detail = Resume.objects.get(pk=pk)
        return render(request, 'enroll/candidate_detail.html',{'candidate':candidate_detail})

        