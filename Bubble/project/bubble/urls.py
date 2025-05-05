from django.urls import path
from bubble import views
from .views import ChatRoomDeleteView, ChatRoomDetailView

urlpatterns = [

    path('Index', views.Index, name= 'Index'),
    path('Chatroom/', views.Chatroom_list, name='Chatroom_list'),
    path('Chatroom/<int:pk>/', ChatRoomDetailView.as_view(), name = 'Chatroom_detail'),
    path('Chatroom/<int:pk>/delete', ChatRoomDeleteView.as_view(), name = 'Chatroom_delete'),

    path('Create-room', views.create_chatroom, name= 'create_chatroom'),
    path('Registration', views.registration, name='registration'),
    path('Log-in', views.Sign_in, name= 'Login'),
    path ('log-out', views.sign_out, name= 'logout')
    #path ('Chatroom/login', views.Login, name= "Login")
]

#views.Chatroom_detail