from django.urls import reverse, resolve
from django.test import Client, SimpleTestCase, TestCase
from user.views import dashboard, adminview, addadmin, editadmin, updateadmin, deleteadmin

class TestUrls(SimpleTestCase):
    def test_case_dashboard_url(self):
        url=reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)

    def test_case_adminview_url(self):
        url=reverse('adminview')
        self.assertEquals(resolve(url).func, adminview)

    def test_case_addadmin_url(self):
        url=reverse('addadmin')
        self.assertEquals(resolve(url).func, addadmin)

    def test_case_editadmin_url(self):
        url=reverse('editadmin', args=[1])
        self.assertEquals(resolve(url).func, editadmin)

    def test_case_updateadmin_url(self):
        url=reverse('updateadmin', args=[1])
        self.assertEquals(resolve(url).func, updateadmin)
        
    def test_case_deleteadmin_url(self):
        url=reverse('deleteadmin', args=[1])
        self.assertEquals(resolve(url).func, deleteadmin)

    
class TestViews(TestCase):
    def test_case_adminview_views(self):
        client=Client()
        url=reverse('adminview')

        response=client.get(url)
        print(response)
        self.assertTemplateUsed(response, 'admin/view.html')