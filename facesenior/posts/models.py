from django.db import models
from users  import models as users

class posts(models.Model):
 post_id   =  models.AutoField(primary_key=True)
 post_desc = models.CharField(max_length=100)
 user_id = models.ForeignKey(users.User, on_delete=models.CASCADE )

