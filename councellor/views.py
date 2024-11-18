from django.shortcuts import render
from .models import Councellor, complaint,feedback, rating
from django.views import View

# Create your views here.
class ViewCouncellor(View):
    def get(self,request):
        abc=Councellor.objects.all()
        return render(request,'administrator/verify councellor.html',{'key':abc})
    
class Viewfeedback(View):
    def get(self,request):
        abc=feedback.objects.all()
        return render(request,'administrator/feedback.html',{'key':abc})

class Viewrating(View):
    def get(self,request):
        abc=rating.objects.all()
        return render(request,'administrator/rating.html',{'key':abc})
        
class Viewcomplaint(View):
    def get(self,request):
        abc=complaint.objects.all()
        return render(request,'administrator/complaint.html',{'key':abc})

class replay(View):
    def get(self,request,id):
        abc=complaint.objects.get(id=id)
        print(abc)
        return render(request,'administrator/replay.html',{'key':abc})
    def post(self,request,id):
        abc=complaint.objects.get(id=id)
        form=complaint form(request.POST, instance=abc)

        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("sucessfull replied'');window.location="/giftadmin/viewcomplient"</script>''')
        else:
            print(form.errors)
            return Httpresponse(<script>alert("failed to reply.please check form errors.");window.location="/giftadmin/viewcomplient")
