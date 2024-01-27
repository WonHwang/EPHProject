from django.db import models

# 메인 게시판 모델
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 최초 생성 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정 시간

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 게시글 삭제시 댓글도 삭제
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 최초 생성 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정 시간

    def __str__(self):
        return self.content