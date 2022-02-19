from django.urls import reverse, resolve
from django.test import Client, SimpleTestCase, TestCase
from guitar.views import guitarview, guitaradd, guitaredit, guitarupdate, guitardelete

class TestUrls(SimpleTestCase):
    def test_case_guitarview_url(self):
        url=reverse('guitarview')
        self.assertEquals(resolve(url).func, guitarview)

    def test_case_guitaradd_url(self):
        url=reverse('guitaradd')
        self.assertEquals(resolve(url).func, guitaradd)

    def test_case_guitaredit_url(self):
        url=reverse('guitaredit', args=[1])
        self.assertEquals(resolve(url).func, guitaredit)

    def test_case_guitarupdate_url(self):
        url=reverse('guitarupdate', args=[1])
        self.assertEquals(resolve(url).func, guitarupdate)

    def test_case_guitardelete_url(self):
        url=reverse('guitardelete', args=[1])
        self.assertEquals(resolve(url).func, guitardelete) 

    
class TestViews(TestCase):
    def test_case_guitarview_views(self):
        client=Client()
        url=reverse('guitarview')

        response=client.get(url)
        print(response)
        self.assertTemplateUsed(response, 'guitar/view.html')