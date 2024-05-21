from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Travel, Camping, Leisure, Cooking
from .serializers import (
    TravelSerializer, 
    CampingSerializer,
    LeisureSerializer,
    CookingSerializer,
)

class BaseListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]  # 모든 요청을 허용

class TravelList(BaseListView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class TravelDetail(BaseDetailView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class CampingList(BaseListView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer

class CampingDetail(BaseDetailView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer

class LeisureList(BaseListView):
    queryset = Leisure.objects.all()
    serializer_class = LeisureSerializer

class LeisureDetail(BaseDetailView):
    queryset = Leisure.objects.all()
    serializer_class = LeisureSerializer

class CookingList(BaseListView):
    queryset = Cooking.objects.all()
    serializer_class = CookingSerializer

class CookingDetail(BaseDetailView):
    queryset = Cooking.objects.all()
    serializer_class = CookingSerializer
