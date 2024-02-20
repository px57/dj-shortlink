from django.test import TestCase
from django.urls import reverse


class ShortlinkTest(TestCase):
    def test_generate(self):
        """
        Test the shortlink.
        """
