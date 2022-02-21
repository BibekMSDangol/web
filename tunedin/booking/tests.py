from django.urls import reverse, resolve
from django.test import Client, SimpleTestCase, TestCase
from booking.views import bookingdelete, bookingview, bookingadd

class TestUrls(SimpleTestCase):
    def test_case_bookingview_url(self):
        url=reverse('bookingview')
        self.assertEquals(resolve(url).func, bookingview)

    def test_case_bookingadd_url(self):
        url=reverse('bookingadd')
        self.assertEquals(resolve(url).func, bookingadd)

    def test_case_bookingdelete_url(self):
        url=reverse('bookingdelete', args=[1])
        self.assertEquals(resolve(url).func, bookingdelete)

    
class TestViews(TestCase):
    def test_case_bookingview_views(self):
        client=Client()
        url=reverse('bookingview')
        
        response=client.get(url)
        print(response)
        self.assertTemplateUsed(response, 'booking/view.html')