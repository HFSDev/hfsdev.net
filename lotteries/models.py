from django.db import models
from states.models import City

class WinningCity(models.Model):
    '''
    This entity is needed to store cities when they win in a duplicating manner
    If the same city wins a single contest twice, there's no way to tell it if 
    we don't differentiate the objects.
    '''
    city = models.ForeignKey(City)
    # a differentiator integer just to set this winning city a part.
    differentiator = models.PositiveSmallIntegerField()

class LotoDraw(models.Model):
    '''
    Entity that maps a real draw from the Lotofacil game. Whoever gets 15 
    numbers right out of 25, wins the pot.
    '''
    draw_number = models.PositiveIntegerField(unique=True)
    date = models.DateField()
    number_1 = models.PositiveSmallIntegerField()
    number_2 = models.PositiveSmallIntegerField()
    number_3 = models.PositiveSmallIntegerField()
    number_4 = models.PositiveSmallIntegerField()
    number_5 = models.PositiveSmallIntegerField()
    number_6 = models.PositiveSmallIntegerField()
    number_7 = models.PositiveSmallIntegerField()
    number_8 = models.PositiveSmallIntegerField()
    number_9 = models.PositiveSmallIntegerField()
    number_10 = models.PositiveSmallIntegerField()
    number_11 = models.PositiveSmallIntegerField()
    number_12 = models.PositiveSmallIntegerField()
    number_13 = models.PositiveSmallIntegerField()
    number_14 = models.PositiveSmallIntegerField()
    number_15 = models.PositiveSmallIntegerField()
    total_collected = models.DecimalField(decimal_places=2, max_digits=19)
    total_winners = models.PositiveIntegerField()
    winning_cities = models.ManyToManyField (WinningCity)
    prize_per_winner = models.DecimalField(decimal_places=2, max_digits=19)
    prize_for_next_draw = models.DecimalField(decimal_places=2, max_digits=19)

    def get_numbers_list(self):
        return [self.number_1, self.number_2, self.number_3,
                self.number_4, self.number_5, self.number_6,
                self.number_7, self.number_8, self.number_9,
                self.number_10, self.number_11, self.number_12,
                self.number_13, self.number_14, self.number_15]