from django.db import models

from accounts.models import Account
import os
import random
import time

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return ext

def upload_image_path(instance, filename):
    ext = get_file_ext(filename)
    new_filename = str(time.time()).split('.')
    new_filename = new_filename[0] + new_filename[1]
    user = instance.account.user.username
    final_filename = '{}-{}{}'.format(user, new_filename, ext)
    return "posts/{}/{}".format(
			user,
            final_filename
            )

class Post(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)

	# post type
	post_types = [
		('SEARCH', 'search'),
		('RENT', 'rent'),
		('BOTH', 'both'),
	]
	type = models.CharField(
        max_length=10,
        choices=post_types,
        default="BOTH",
    )

	# communication ways
	email = models.BooleanField(default=False)
	phone = models.BooleanField(default=False)
	facebook = models.BooleanField(default=False)
	twitter = models.BooleanField(default=False)
	linkedin = models.BooleanField(default=False)

	def __str__(self):
		return self.title if self.title else self.description
	