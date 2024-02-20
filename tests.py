from django.test import TestCase
from django.urls import reverse


class ShortlinkTest(TestCase):
    def test_shortlink(self):
        """
        Test the shortlink.
        """