from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu , Booking
# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(ListCreateAPIView):
    serializer_class=MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    data = {"message": "this view is protected"}
    return Response(data)
