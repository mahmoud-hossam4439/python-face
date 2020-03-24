from django.db import models
from users  import models as users

class friends(models.Model):
    user_id = models.ForeignKey(users.User, on_delete=models.CASCADE )
    frind_id = models.ForeignKey(users.User, on_delete=models.CASCADE, related_name='onwer')


