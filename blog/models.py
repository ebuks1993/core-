from email.policy import default
from mailbox import mbox
from tokenize import blank_re
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    posted_date = models.DateTimeField(auto_now_add=True,null=True)
    title = models.CharField( max_length=350)
    slug = models.SlugField(null=True,blank=True)
    post_img = models.ImageField(null=True,blank=True,default='default.png')
    body = models.TextField(null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Article,self).save(*args,**kwargs)
  
    def __str__(self):
        return self.title

class CommentReaction(models.Model):
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    thecomment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    reaction = models.ForeignKey(CommentReaction, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null=True)

class Reply(models.Model):
    replier = models.ForeignKey(User, on_delete=models.CASCADE)
    thereply = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    reaction = models.ForeignKey(CommentReaction, on_delete=models.CASCADE)
    thecomment = models.ForeignKey(Comment, on_delete=models.CASCADE)
   




