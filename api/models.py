from django.db import models

# Create your models here.

class Note(models.Model):
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #__str__()で呼び出すことでbodyの内容を50文字まで取り出せる
        return self.body[0:50]

    class Meta:
        #インスタンスをあるfield値で並び替え'-〇〇'をつけることで昇順
        ordering=['-updated']
