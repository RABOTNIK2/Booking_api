from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['put'])
    def add_to_fav(self, request):
        try:
            user = User.objects.get(pk = request.data['id'])
            user_fav = User.objects.get(pk = request.data['id']).favorite.all()
            hotel = Hotel.objects.get(pk = request.data['hotel_id'])
            user_list = list(user_fav)
            user_list.append(hotel)
            user.favorite.set(user_list)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['put'])
    def del_from_fav(self, request):
        try:
            user = User.objects.get(pk = request.data['id'])
            hotel = Hotel.objects.get(name = request.data['q'])
            user_fav = User.objects.get(pk = request.data['id']).favorite.all()
            user_list = list(user_fav)
            index = 0
            if len(user_list)!=0:        
                for i in user_list:
                    if i.name == hotel.name:
                        index = user_list.index(i)
                        break
                user_list.pop(index)
                user.favorite.set(user_list)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response({'message': 'Непредвиденная ошибка'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Пользователь не найден'})
                
        
class BookingViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            hotel_book = Hotel.objects.get(pk = request.data['hotel'])
            print(hotel_book)
            if (hotel_book.single_room - int(request.data['quantity_single_room'])) >=0 and (hotel_book.double_room - int(request.data['quantity_double_room'])) >=0 and (hotel_book.multi_room - int(request.data['quantity_multi_room'])) >=0:
                serializer = BookingSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()  
                    hotel_book.single_room -= int(request.data['quantity_single_room'])
                    hotel_book.double_room -= int(request.data['quantity_double_room'])
                    hotel_book.multi_room -= int(request.data['quantity_multi_room'])
                    hotel_book.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
            else:
                return Response({'message': 'Извините мест нет'}, status=status.HTTP_400_BAD_REQUEST)
        except Hotel.DoesNotExist:
            return Response({'message': 'Такого отеля не существует'}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            serializer = BookingSerializer(booking, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            booking = Booking.objects.get(pk=pk)
            booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ReviewViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            hotel = Hotel.objects.get(pk = request.data['hotel_review'])
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                reviews = Review.objects.filter(hotel_review = request.data['hotel_review'])
                points = 0 
                for i in reviews:
                    points += i.reaction
                rating = points/len(reviews)
                hotel.rating = rating
                hotel.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Hotel.DoesNotExist:
            return Response({'message': 'Ошибка'}, status=status.HTTP_404_NOT_FOUND)    
        
    def retrieve(self, request, pk=None):
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            review = Review.objects.get(pk=pk)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

# Create your views here.
