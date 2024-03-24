from django.test import TestCase


from django.contrib.auth.models import User

# from .models import Profile
# Create your tests here.


class TestProfile(TestCase):
    def setUp(self):
        self.response = self.client.post(
            "/register/",
            {
                "first_name": "luxannacrown",
                "last_name": "crownguard",
                "username": "luxannacrown",
                "email": "lux@riotgames.com",
                "password1": "demacia12345",
                "password2": "demacia12345",
            },
        )

    def test_profile_exists(self):
        user = User.objects.get(username="luxannacrown")

        assert isinstance(user.profile.id, int)

    def test_redirect(self):
        self.response.status_code == 302
