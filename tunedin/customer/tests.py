from audioop import reverse
from pydoc import resolve
from urllib import response
from django.urls import reverse, resolve
from django.test import Client, SimpleTestCase, TestCase
from customer.views import customerview, addcustomer, register, login, index, editcustomer, updatecustomer, deletecustomer
# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_customerview_url(self):
        url=reverse('customerview')
        self.assertEquals(resolve(url).func, customerview)

    def test_case_addcustomer_url(self):
        url=reverse('addcustomer')
        self.assertEquals(resolve(url).func, addcustomer)

    def test_case_adminregister_url(self):
        url=reverse('adminregister')
        self.assertEquals(resolve(url).func, register)

    def test_case_adminlogin_url(self):
        url=reverse('adminlogin')
        self.assertEquals(resolve(url).func, login)

    def test_case_index_url(self):
        url=reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_case_editcustomer_url(self):
        url=reverse('editcustomer', args=[1])
        self.assertEquals(resolve(url).func, editcustomer)

    def test_case_updatecustomer_url(self):
        url=reverse('updatecustomer', args=[1])
        self.assertEquals(resolve(url).func, updatecustomer)

    def test_case_deletecustomer_url(self):
        url=reverse('deletecustomer', args=[1])
        self.assertEquals(resolve(url).func, deletecustomer)



class TestViews(TestCase):
    def test_case_customerview_views(self):
        client=Client()
        url=reverse('customerview')

        response=client.get(url)
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/view.html')