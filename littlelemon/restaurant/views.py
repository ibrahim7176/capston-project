from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu , Booking
# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(ListCreateAPIView):
    serializer_class=MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer