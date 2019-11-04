from django.db import models

# Create your models here.
class TitleWords(models.Model):
    # id
    id = models.IntegerField(primary_key=True)
    # type1
    type1 = models.CharField(max_length=32)
    # type2
    type2 = models.CharField(max_length=32)
    # type3
    type3 = models.CharField(max_length=32)
    # word
    word = models.CharField(max_length=32)

class TitleChains(models.Model):
    # id1
    id1 = models.IntegerField()
    # id2
    id2 = models.IntegerField()
    # num
    num = models.IntegerField()