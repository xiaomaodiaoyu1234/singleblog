from django.db import models

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    def __str__(self):
        return self.tag_name
    class Meta:
        verbose_name_plural = '标签'

class Cagr(models.Model):
    cag_name = models.CharField(max_length=100)
    def __str__(self):
        return self.cag_name
    class Meta:
        verbose_name_plural = '文章'


class Post(models.Model):
    title = models.CharField('标题',max_length=100)
    content = models.TextField('内容')
    desc = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag)
    con = models.ForeignKey(Cagr)
    def __str__(self):
        return self.title
    def myca(self):
        return self.con
    myca.short_description = '详情'
    def mytag(self):
        return ' '.join([i.tag_name for i in self.tag.all()])
    mytag.short_description = "标签"
    class Meta:
        verbose_name_plural = '详情'
        ordering = ['-id']


