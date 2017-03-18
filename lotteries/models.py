from django.db import models
from states.models import City

class LotoDraw(models.Model):
    draw_number = models.PositiveIntegerField(unique=True)
    date = models.DateField()
    number_1 = models.PositiveSmallIntegerField(max_value=25)
    number_2 = models.PositiveSmallIntegerField(max_value=25)
    number_3 = models.PositiveSmallIntegerField(max_value=25)
    number_4 = models.PositiveSmallIntegerField(max_value=25)
    number_5 = models.PositiveSmallIntegerField(max_value=25)
    number_6 = models.PositiveSmallIntegerField(max_value=25)
    number_7 = models.PositiveSmallIntegerField(max_value=25)
    number_8 = models.PositiveSmallIntegerField(max_value=25)
    number_9 = models.PositiveSmallIntegerField(max_value=25)
    number_10 = models.PositiveSmallIntegerField(max_value=25)
    number_11 = models.PositiveSmallIntegerField(max_value=25)
    number_12 = models.PositiveSmallIntegerField(max_value=25)
    number_13 = models.PositiveSmallIntegerField(max_value=25)
    number_14 = models.PositiveSmallIntegerField(max_value=25)
    number_15 = models.PositiveSmallIntegerField(max_value=25)
    total_collected = models.DecimalField(decimal_places=2, max_digits=19)
    total_winners = models.PositiveIntegerField()
    winning_cities = models.ManyToManyRel(City)
    prize_per_winner = models.DecimalField(decimal_places=2, max_digits=19)
    prize_for_next_draw = models.DecimalField(decimal_places=2, max_digits=19)

    def get_numbers_list(self):
        return [self.number_1, self.number_2, self.number_3,
                self.number_4, self.number_5, self.number_6,
                self.number_7, self.number_8, self.number_9,
                self.number_10, self.number_11, self.number_12,
                self.number_13, self.number_14, self.number_15]

