from django.shortcuts import render
from django.http import JsonResponse
from .models import Reservation, Guest, Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReservationSerializer, GuestSerializer, MovieSerializer
from rest_framework import status , filters
from rest_framework.views import APIView
from rest_framework import mixins, generics , viewsets

# Create your views here.


# without REST and no model queryset FBV

def no_rest_no_model(request):
    guests = [
        {
        'id': 1,
        'name': 'omar',
        'email': 'omar@gmail.com'
        },
        {
        'id': 2,
        'name': 'reem',
        'email': 'reem@gmail.com'
        },
        {
        'id': 3,
        'name': 'nour',
        'email': 'nour@gmail.com'
        },
    ]
    return JsonResponse(guests, safe=False)
      
# Model Data default and without REST  

def no_rest_from_model(request):
    guests = Guest.objects.all()
    response = {
        'guests': list(guests.values('name', 'email'))
    }
    return JsonResponse(response)

# 3.1 - function based view

@api_view(['GET', 'POST'])
def FBV_list(request):
    # GET list of guests
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    # POST a new guest
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 3.2 - function based view with pk    
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # GET 
        if request.method == 'GET':
            serializer = GuestSerializer(guest)
            return Response(serializer.data)
        
        # PUT 
        elif request.method == 'PUT':
            serializer = GuestSerializer(guest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # DELETE
        if request.method == 'DELETE':
            guest.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
            
# 4.1 Class based view

class CBV_View(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 4.2 Class based view with pk

class CBV_Pk(APIView):
    def get(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# 5.1 - mixins list
class Mixin_List(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
#5.2 - mixins list with pk
class Mixin_Pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)    


#6.1 - generic views list
class Generic_List(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

#6.2 - generic views list with pk
class Generic_Pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


# 7.1 - viewsets
class viewsets_guests(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# 7.2 - viewsets with pk
class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_field = ['movie']
    
#7.3
class viewsets_reservation(viewsets.ModelViewSet):
        queryset = Reservation.objects.all()
        serializer_class = ReservationSerializer    
        
        
# 8.1 - find movie
@api_view(['GET'])
def find_movie(request):
    if request.method == 'GET':
        movies = Movie.objects.filter(movie=request.data['movie'],
        hall = request.data['hall'])
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
# 9  create new reservation
api_view(['POST'])
def create_reservation(request):
        movie = Movie.objects.get(
            hall = request.data['hall'],
            movie = request.data['movie'],
        )
        guest = Guest()
        guest.name = request.data['name']
        guest.phone = request.data['phone']
        guest.save()
        reservation = Reservation()
        reservation.guest = guest
        reservation.movie = movie
        reservation.save()
        return Response(status=status.HTTP_201_CREATED)
       