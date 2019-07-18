from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment (models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    #author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    #get_user_model : 커스텀모델, 커스텀 유저를 넣거나 없으면 그냥 유저를 받는다.
    #author : model.SET_NULL : 연결된 foreinkey, 즉 유저가 삭제되어도 코멘트를 null로 바꾸고 남겨놓는다. 단 null=True가 필요하다.
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return (self.author.username if self.author else "무명") + "의 댓글"