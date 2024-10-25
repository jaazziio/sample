from django.shortcuts import render
from django.views import View

# Create your views here.
# ////////////////////////////// admin //////////////////// 
class AdminDashboard(View):
    def get(self,request):
        return render(request,"administrator/adminDashboard.html")    
class ProductApprove(View):
    def get(self,request):
        return render(request,"administrator/aapprove.html")    
class ProductFeedback(View):
    def get(self,request):
        return render(request,"administrator/feedback.html")
class ForgetPassword(View):
    def get(self,request):
        return render(request,"administrator/forgetPassword.html") 
class ViewUser(View):
    def get(self,request):
        return render(request,"administrator/viewusers.html")
# ////////////////////// manufacture ///////////////////
class ProductAdd(View):
    def get(self,request):
        return render(request,"manufactor/add.html")
class ProductEdit(View):
    def get(self,request):
        return render(request,"manufactor/edit.html")
class ProductManage(View):
    def get(self,request):
        return render(request,"manufactor/manage.html")
class ManufactureDashboard(View):
    def get(self,request):
        return render(request,"manufactor/manufactureDashboard.html")
class Register(View):
    def get(self,request):
        return render(request,"manufactor/Register.html")
class ProductUpdate(View):
    def get(self,request):
        return render(request,"manufactor/update.html")
    

class Login(View):
    def get(self,request):
        return render(request,"login.html")
class MainPage(View):
    def get(self,request):
        return render(request,"mainpage.html")    