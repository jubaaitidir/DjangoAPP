
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Profile (models.Model):
#     app_label = 'Profile'
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     firstname = models.TextField(max_length=500, blank=True)
#     lastname = models.TextField(max_length=500, blank=True)
#     account_type = models.TextField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     # 'address': {'nbr': 84, 'street': 'rue Tabakayo', 'apprt': '' ,'zib_code': 95684, 'city': 'Chinta', 'country':'Dreamland'}
#     address_nbr = models.CharField(max_length=20, blank=True)    
#     address_street = models.TextField(max_length=100, blank=True)
#     address_apprt = models.TextField(max_length=50, blank=True)
#     address_zib_code = models.TextField(max_length=5, blank=True)
#     address_city = models.TextField(max_length=50, blank=True)
#     address_country = models.TextField(max_length=50, blank=True)

#     def __str__(self):
#         return self.app_label

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
