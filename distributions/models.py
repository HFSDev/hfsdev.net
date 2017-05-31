from django.db import models
from lotteries.models import LotoDraw
# Create your models here.
class LotoDistribution(models.Model):
    '''
    Holds the number distribution over time. Since getting all draws from
    database is computer consuming, we do it only once per draw when the system
    loads the last draw from the web.
    '''
    last_draw = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)
    number_1 = models.PositiveIntegerField()
    number_2 = models.PositiveIntegerField()
    number_3 = models.PositiveIntegerField()
    number_4 = models.PositiveIntegerField()
    number_5 = models.PositiveIntegerField()
    number_6 = models.PositiveIntegerField()
    number_7 = models.PositiveIntegerField()
    number_8 = models.PositiveIntegerField()
    number_9 = models.PositiveIntegerField()
    number_10 = models.PositiveIntegerField()
    number_11 = models.PositiveIntegerField()
    number_12 = models.PositiveIntegerField()
    number_13 = models.PositiveIntegerField()
    number_14 = models.PositiveIntegerField()
    number_15 = models.PositiveIntegerField()