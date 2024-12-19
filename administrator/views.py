from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *
from django.views import View

# Create your views here.
class VerifyCouncellor(View):
    def get(self,request):
        abc=Councellor.objects.all()
        return render(request,'administrator/verify_councellor.html',{'key':abc})
class Accept_Councellor(View):
    def get(self, request, C_id):
        try:
            Coun = Councellor.objects.get(id=C_id)
            print(Coun)  # Fetch the instance
            Coun.LOGINID.type = 'Councellor'  # Update the status
            Coun.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Accepted");window.location="/Verify_Councellor"</script>''')  
        except Logintable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Councellor not found", status=404)
        

class Reject_Councellor(View):
    def get(self, request, C_id):
        try:
            Coun = Councellor.objects.get(id=C_id)  # Fetch the instance
            Coun.LOGINID.type = 'Rejected'  # Update the status
            Coun.LOGINID.save()  # Save the changes
            return HttpResponse('''<script>alert("successfully Rejected");window.location="/"Verify_Councellor</script>''')  
        except Logintable.DoesNotExist:
            # Handle the case where the shop doesn't exist
            return HttpResponse("Shop not found", status=404)
    
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
        form=complaint_form(request.POST, instance=abc)

        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("sucessfull replied'');window.location="/giftadmin/viewcomplient"</script>''')
        else:
            print(form.errors)
            return HttpResponse('''<script>alert("failed to reply.please check form errors.");window.location="/giftadmin/viewcomplient"</script>''')

class adminhomepage(View):
    def get(self,request):
     return render(request,'administrator/adminhomepage.html')
    
class login(View):
    def get(self,request):
     return render(request,'administrator/login.html')
    def post(self,request):
        print("hhhh")
        username = request.POST['username']
        password = request.POST['password']
        login_obj = Logintable.objects.get(username=username, password=password)
        if login_obj.type == "admin":
            return render(request,'administrator/adminhomepage.html')
class ratingandfeedback(View):
    def get(self,request):
       return render(request,'administrator/ratingandfeedback.html')
     
class replaybox(View):
    def get(self,request):
       return render(request,'replaybox.html/')
    
class verify_user(View):
    def get(self,request):
       return render(request,'administrator/verify_users.html/') 
       
class chatwithuser(View):
    def get(self,request,):
       return render(request,'chatwithuser/')   

class councellorregister(View):
    def get(self,request,):
       return render(request,'councellor/councellorregister.html')
    def post(self,request,):
        s=councellor_form(request.POST)
        if s.is_valid():
            s.save(commit=False)
            c=Logintable.objects.create(username=request.POST['username'],password=request.POST['password'],type='councellor')
            s.LOGINID=c
            s.save()
        return HttpResponse('''<script>alert("ok");window.location="/"</script>''')
class counsellorHomepage(View):
    def get(self,request,):
       return render(request,'counsellorHomepage.html/')

class requestfromuser(View):
    def get(self,request,):
       return render(request,'requestfromuser.html/')


class uploadmotivationalthoughts(View):
    def get(self,request,):
       return render(request,' uploadmotivationalthoughts.html/')

class uploadmotivationalVideos(View):
    def get(self,request,):
       return render(request,' uploadmotivationalVideos.html/')
                
class videocallwithuser(View):
    def get(self,request,):
       return render(request,' videocallwithuser.html/')

    
class applicationandrating(View):
    def get(self,request):
       return render(request,'administrator/applicationandrating.html')
    

    
    
