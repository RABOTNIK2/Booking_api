from django.test import TestCase
from .models import *
from django.urls import reverse
from urllib.parse import urlencode

class BookingTest(TestCase):
    def setUp(self):
        self.hotel = Hotel.objects.create(
            name = 'Koleno',
            description = 'kkfkdjgdjkgjdkg',
            image = 'dgdfgdfhdfhffdj',
            adress = 'gfdghfgjndfn',
            contacts = '92849753 dfdsg',
            amenities = 'dsggdfhdggdjfgjg',
            is_animals = True,
            single_room = 12,
            double_room = 10,
            multi_room = 2,
            price_per_night = 35366,
        )
        self.data = {'username': 'gnida', 'first_name': 'Pidrila', 'last_name': 'Jopeshnik', 'password': 'gnidovski', 'phone': 8745930563}
        self.user = User.objects.create_user(**self.data)
        self.user.favorite.set([self.hotel])
        
    def test_book_create(self):
        data = urlencode({
            'user_booking':self.user.pk,
            'hotel':self.hotel.pk,
            'arrival_date': '2024-07-11',
            'date_of_dispatch': '2025-07-11',
            'quantity_single_room': 1,
            'quantity_double_room': 2,
            'quantity_multi_room': 0,
        })
        response = self.client.post(reverse('bookin-list'), data, content_type="application/x-www-form-urlencoded")
        updated_hotel = Hotel.objects.get(pk = self.hotel.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_hotel.single_room, 11)
        self.assertEqual(updated_hotel.double_room, 8)
        self.assertEqual(updated_hotel.multi_room, 2)
        self.assertTrue(str(self.hotel.pk) in response.content.decode())
        
    # def test_add_to_fav(self):
    #     data = urlencode({'id': self.user.pk, 'hotel_id':self.hotel.pk})
    #     response = self.client.put(reverse('user-add-to-fav'), data, content_type="application/x-www-form-urlencoded")
    #     self.assertTrue(str(self.hotel.pk) in response.content.decode())
        
    def test_del_from_fav(self):
        data = urlencode({
            'id': self.user.pk,
            'q': self.hotel.name,
        })
        response = self.client.put(reverse('user-del-from-fav'), data, content_type="application/x-www-form-urlencoded")   
        self.assertIn(str(self.hotel.pk), response.content.decode())
        
    def test_review_create(self):
        data = urlencode({
            "author":self.user.pk,
            "hotel_review": self.hotel.pk,
            "content": "jgjfnjndkhkdh",
            "reaction":4,
        })
        response = self.client.post(reverse('review-list'), data, content_type="application/x-www-form-urlencoded")
        updated_hotel = Hotel.objects.get(pk = self.hotel.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(self.user.pk), response.content.decode())
        self.assertEqual(updated_hotel.rating, 4)

# Create your tests here.
