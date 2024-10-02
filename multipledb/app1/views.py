from django.shortcuts import render,redirect
from app1.forms import Model1Form,Model2Form
# Create your views here.

def combinated_forms_view(request):
    if request.method=='POST':
        form1=Model1Form(request.POST)
        form2=Model2Form(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return  render( request,'sucess.html')
    else:
        form1=Model1Form()
        form2=Model2Form()
    return render(request,'combined_form.html',{'form1':form1,'form2':form2})

def sucess_url(request):
    return render( request,'sucess.html')
