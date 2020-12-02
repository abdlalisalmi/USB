from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=50, blank=True, null=True)
	avatar = models.ImageField(upload_to='users/avatar/', blank=True, null=True)
	email = models.EmailField(max_length=254, blank=True, null=True)
	phone = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)

	# Social Media Accounts
	facebook = models.URLField(blank=True, null=True)
	twitter = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.user.username if self.user.username else self.full_name


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
	if created:
		Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
	instance.account.save()
	