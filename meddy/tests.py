from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Procedure
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(id=1,prof_user=self.new_user,bio='Test Bio',contact_info='0723030837',profile_Id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_bio(self):
        self.new_profile.save_profile()
        self.new_profile = Profile.objects.get(id=1)
        profile = self.new_profile
        profile.update_bio('updated user-bio')
        self.updated_profile = Profile.objects.get(id=1)
        self.assertEqual(self.updated_profile.bio,'updated user-bio')

class ProcedureTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(id=1,prof_user=self.new_user,bio='Test Bio',contact_info='0723030837',profile_Id=1)
        self.new_profile.save_profile()
        self.new_procedure = Procedure(id=1,title='title',details='details',link='www.link.com',user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_procedure,Procedure))

    def test_save_instance(self):
        self.new_procedure.save_procedure()
        procedure = Procedure.objects.all()
        self.assertTrue(len(procedure)>0)

    def test_delete_profile(self):
        self.new_procedure.delete_procedure()
        procedure = Procedure.objects.all()
        self.assertTrue(len(procedure)==0)

    def test_fetch_procedure(self):
        self.new_procedure.save_procedure()
        procedure = Procedure.fetch_all_images()
        self.assertTrue(len(procedure)>0)

    def test_find_procedure(self):
        self.new_procedure.save_procedure()
        procedure = Procedure.get_single_procedure(self.new_procedure.id)
        self.assertTrue(procedure == self.new_procedure)