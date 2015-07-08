# -*- coding: utf-8 -*-
from django.test import TestCase

from django.contrib.auth import get_user_model
from . import models

class TestProfileModel(TestCase):

    def test_profile_creation(self):
        User = get_user_model()
        # New user created
        user = User.objects.create(
            username="taskbuster", password="django-tutorial")
        #Check thath a Profile instance has been created
        self.assertIsInstance(user.profile, models.Profile)
        # Call the save method of the use to activate the signal
        # again, and check thath it doesn't try to create another
        # profile instance
        user.save()
        self.assertIsInstance(user.profile, models.Profile)
