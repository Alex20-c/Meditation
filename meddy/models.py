# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Procedure(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='procedure_pics',blank=True)
    user_procedure_id = models.IntegerField(default=0)
    steps= models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    process = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def save_procedure(self):
        self.save()

    def delete_procedure(self):
        self.delete()

    @classmethod
    def fetch_all_images(cls):
        all_images = Procedure.objects.all()
        return all_images

    @classmethod
    def search_procedure_by_title(cls,search_term):
        procedure = cls.objects.filter(title__icontains=search_term)
        return procedure

    @classmethod
    def get_single_procedure(cls, procedure):
        procedure = cls.objects.get(id=procedure)
        return procedure

    class Meta:
        ordering = ['-id']

    
    
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField()
    contact_info = models.CharField(max_length=200,blank=True)
    profile_Id = models.IntegerField(default=0)
    all_procedure= models.ForeignKey('Procedure',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()
