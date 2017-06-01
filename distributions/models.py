from django.db import models
from lotteries.models import LotoDraw
# Create your models here.
class LotoDistribution(models.Model):
    '''
    Holds the number distribution over time. Since getting all draws from
    database is computer consuming, we do it only once per draw when the system
    loads the last draw from the web.
    '''
    draw_marker = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)
    count_number_1 = models.PositiveIntegerField()
    count_number_2 = models.PositiveIntegerField()
    count_number_3 = models.PositiveIntegerField()
    count_number_4 = models.PositiveIntegerField()
    count_number_5 = models.PositiveIntegerField()
    count_number_6 = models.PositiveIntegerField()
    count_number_7 = models.PositiveIntegerField()
    count_number_8 = models.PositiveIntegerField()
    count_number_9 = models.PositiveIntegerField()
    count_number_10 = models.PositiveIntegerField()
    count_number_11 = models.PositiveIntegerField()
    count_number_12 = models.PositiveIntegerField()
    count_number_13 = models.PositiveIntegerField()
    count_number_14 = models.PositiveIntegerField()
    count_number_15 = models.PositiveIntegerField()
    count_number_16 = models.PositiveIntegerField()
    count_number_17 = models.PositiveIntegerField()
    count_number_18 = models.PositiveIntegerField()
    count_number_19 = models.PositiveIntegerField()
    count_number_20 = models.PositiveIntegerField()
    count_number_21 = models.PositiveIntegerField()
    count_number_22 = models.PositiveIntegerField()
    count_number_23 = models.PositiveIntegerField()
    count_number_24 = models.PositiveIntegerField()
    count_number_25 = models.PositiveIntegerField()

    def to_list(self):
        return [
            (1,  self.count_number_1),
            (2,  self.count_number_2),
            (3,  self.count_number_3),
            (4,  self.count_number_4),
            (5,  self.count_number_5),
            (6,  self.count_number_6),
            (7,  self.count_number_7),
            (8,  self.count_number_8),
            (9,  self.count_number_9),
            (10, self.count_number_10),
            (11, self.count_number_11),
            (12, self.count_number_12),
            (13, self.count_number_13),
            (14, self.count_number_14),
            (15, self.count_number_15),
            (16, self.count_number_16),
            (17, self.count_number_17),
            (18, self.count_number_18),
            (19, self.count_number_19),
            (20, self.count_number_20),
            (21, self.count_number_21),
            (22, self.count_number_22),
            (23, self.count_number_23),
            (24, self.count_number_24),
            (25, self.count_number_25)]
    
    def to_sorted_list(self):
        return sorted(self.to_list(), key=lambda   count: count[1])
