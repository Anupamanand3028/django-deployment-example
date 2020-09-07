from django.shortcuts import render
# from django.http import HttpResponse
from AppTwo.models import ExUser
from .forms import FormName
from .forms import NewUserForm
from .forms import UserProfileInfoForm,UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,authenticate,logout
#from .forms import UserProfileInfoForm
# Create your views here.

def index(request):
    context_dict = {'text':'hi, there','number':100}
    return render(request,'AppTwo/index.html',context_dict)

@login_required
def special(request):
    return HttpResponse('You are logged in nice!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def relative(request):
    return render(request,'AppTwo/relative_url_templates.html')

    #return HttpResponse("<em> My Second Project </em>")

def help(request):
    help_dict = {'feed_me':'this is the help page'}
    return render(request, 'AppTwo/help.html',context=help_dict)

def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'AppTwo/register.html',{'user_form':user_form,'profile_form':profile_form, 'registered':registered})


# -----------------not in use--------------------------
# def users(request):
#     user_list = User.objects.order_by('first_name')
#     users_dict = {'users':user_list}
#     return render(request,'AppTwo/users.html',context=users_dict)

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Form Is Invalid!')
    return render(request,'AppTwo/users.html',{'form':form})

def form_name_view(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            # Do something code goes Here
            print('Validation Succesful')
            print('Name : '+form.cleaned_data['name'])
            print('Email : '+form.cleaned_data['email'])
            print('Text :'+form.cleaned_data['text'])
    return render(request,'AppTwo/form_page.html',{'form':form})

# function for user authentication or login
def user_login(request):

    if request.method == 'POST':
        # grab the username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        # using the built-in function for the authentication
        user = authenticate(request,username=username,password=password)

        #check wheter the user is active or not
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print('Someone tried to login and failed')
            print('Username {} and Password {}'.format(username,password))
            return HttpResponse('Invalid Username or Password is Supplied!')
    else:
        return render(request,'AppTwo/login.html')
