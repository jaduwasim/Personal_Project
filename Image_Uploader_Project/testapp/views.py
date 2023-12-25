from django.shortcuts import render
from .forms import ImageForm
from .models import ImageModelClass
# Create your views here.
def Home_View(request):
    img = ImageModelClass.objects.all()
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/home.html',{'form':form, 'img':img})
