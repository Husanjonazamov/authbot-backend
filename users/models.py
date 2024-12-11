from django.db import models




class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)  # Unikal qilish
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    random_code = models.IntegerField()
    is_verified = models.BooleanField(default=False, null=True, blank=True)

    def is_registered(self):
        return self.user_id is not None and User.objects.filter(user_id=self.user_id).exists()
 