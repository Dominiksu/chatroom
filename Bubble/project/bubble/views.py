from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from bubble.models import Chatroom, Messages, User
from django.views.generic import DeleteView
from bubble.forms import Room_Form, User_creation, Log_in
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.decorators.http import require_POST


# Create your views here.


def Index(request):
    return render (request, 'bubble/index.html')


def Chatroom_list(request):
    if request.user.is_authenticated:
        rooms = Chatroom.objects.all()
        
        return render(request, 'bubble/Chatroom_list.html', {'rooms':rooms})
    else: 
        messages.warning(request, 'You need to Log-in to see availible chatrooms')
        return redirect('/Log-in')



def Chatroom_detail(request, pk):
    if request.user.is_authenticated:
        room = get_object_or_404(Chatroom, pk = pk)
        messages = Messages.objects.filter(chat_room = pk).all()
        
        return render(request, 'bubble/Chatroom_detail.html', {"room":room, "messages": messages})
    else: 
        messages.warning(request, 'You cannot chat without being logged in')
        return redirect('/Log-in')


def create_chatroom(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            form = Room_Form(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by = User.objects.get(pk = request.user.id)
                obj.save()
                return redirect('/Chatroom/')
            else:
                print(form.errors)
        else:
            form = Room_Form()
            print('get initiated')
        return render (request, 'bubble/create_room.html', {"form":form})
    else: 
        messages.warning(request, 'You need to Log-in to create chatrooms')
        return redirect('/Log-in')



def registration(request):
    if request.method == "POST":
        form = User_creation(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/Chatroom/")
    else:
        form = User_creation()
    return render (request, 'bubble/Register.html', {"form":form})


def Sign_in(request):
    
    if request.method == 'POST':
        form = Log_in(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password) #dodelat e-mail
            if user:
                login(request, user)
                messages.success(request, f'Hi {user.username.title()}, Log in was succsessful')
                return redirect("Index")
            else:
                messages.error(request, f'You have entered wrong credentials')
                return render(request, 'bubble/Sign_in.html', {'form':form})
    else:
        form = Log_in()
    return render(request, 'bubble/Sign_in.html', {'form':form})


def sign_out(request):
    logout(request)
    messages.success(request, 'you have succcessfully logged out')


class ChatRoomDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/Log-in"
    model = Chatroom
    template_name = "bubble/chatroom_delete.html"
    success_url = "/Chatroom/"



