from django.test import TestCase
from apps.members import models


class TestMembersModel(TestCase):
    def setUp(self):
        self.firstname = "John"
        self.lastname = "Doe"

    def test_dunder_str(self):
        self.assertEqual(str(self.firstname), self.firstname)
