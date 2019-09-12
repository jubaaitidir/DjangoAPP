from django.contrib.auth import authenticate
from django.contrib.auth.models import User

 user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
user.last_name = 'Lennon'
user.save()
print(user)



# user = authenticate(username='john', password='secret')
# if user is not None:
#     # A backend authenticated the credentials
# else:


#     #
# u = User.objects.get(username='john')
# u.set_password('new password')
# u.save()