from django.test import TestCase, Client
from django.urls import reverse
from apps.members.models import Members


class TestResourcesView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_home_page_view_member_count(self):
        Members.objects.create(
            firstname="John",
            lastname="Doe",
            age=25,
            email="Lr2JG@example.com",
            phone="1234567890",
            ability="good",
            league=2,
        )
        expected_member_cnt = 1

        # Act
        response = self.client.get(
            reverse("home-page"),
            HTTP_USER_AGENT="Mozilla/5.0",
            HTTP_CONTENT_TYPE="text/plain",
        )

        # Assert
        self.assertEqual(response.context["member_cnt"], expected_member_cnt)
