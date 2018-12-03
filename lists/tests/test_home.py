from django.test import TestCase
from lists.models import List

class HomePageTest(TestCase):
    """
    Home Page Test, and redirect after adding a new item.
    A new list should be created with a unique id.
    """

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text':'A new list item'})
        new_list = List.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/lists/{new_list.id}/')
