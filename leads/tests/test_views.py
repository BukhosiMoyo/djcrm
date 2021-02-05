from django.test import TestCase
from django.shortcuts import reverse


class LandingPageTest(TestCase):
    """ Check if the landng page returns a 200 get request """
    def test_get(self):
        response = self.client.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")
        
    