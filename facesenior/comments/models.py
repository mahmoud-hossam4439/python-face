from django.db import models
from posts  import models as posts
from users  import models as users

class comments(models.Model):
 comment_id   =  models.AutoField(primary_key=True)
 comment_desc = models.CharField(max_length=100)
 user_id = models.ForeignKey(users.User, on_delete=models.CASCADE )
 post_id = models.ForeignKey(posts.posts, on_delete=models.CASCADE)