from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm,UserprofileChange,UpdatePic
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def signup(request):
    form=SignUpForm()
    registered=False
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True
            
    dict={'form':form, 'registered':registered}
    return render(request,'App_Login/signup.html', context=dict)



def login_page(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            username= form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
    return render(request,'App_Login/login.html',context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:signin'))


@login_required
def profile(request):
    return render(request,'App_Login/profile.html',context={})


@login_required
def UpdateProfile(request):
    current_user=request.user
    form = UserprofileChange(instance=current_user)
    if request.method == 'POST':
        form = UserprofileChange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form=UserprofileChange(instance=current_user)
    return render(request,'App_Login/change_profile.html',context={'form':form})


@login_required
def UpdatePassword(request):
    current_user=request.user
    changed=False
    form= PasswordChangeForm(current_user)
    if request.method=='POST':
        form=PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
    return render(request,'App_Login/pass_change.html',context={'form':form ,'changed':changed})
    return HttpResponseRedirect(reverse('App_Login:signin'))


@login_required
def UpdateProfilePic(request):
    form=UpdatePic()
    if request.method =='POST':
        form=UpdatePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/updateprofilepic.html',context={'form':form})









