from django.test import TestCase, Client
from django.urls import reverse

from main.models import *

class Tests(TestCase):

    def setUp(self):
        self.client = Client()