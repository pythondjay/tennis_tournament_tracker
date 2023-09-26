from django.test import TestCase
from apps.members.form import MembersForm


class TestMembersForm(TestCase):
    def test_form_is_valid(self):
        data = {
            "firstname": "John",
            "lastname": "Doe",
            "age": 25,
            "email": "Lr2JG@example.com",
            "phone": "1234567890",
            "ability": "good",
            "league": 2,
        }

        form = MembersForm(data=data)
        self.assertTrue(form.is_valid())
