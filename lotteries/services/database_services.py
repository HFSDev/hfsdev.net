from lotteries.models import LotoDraw
from lotteries.models import WinningCity
from datetime import date
from time import strptime
from decimal import Decimal
from states.services.states_database_setup import setup_database
from states.models import City
from states.models import State
from states.models import Region
from django.db.models import Max
import pdb

def load_data_from_file(file):
    """
    Deletes all draws and its numbers for reloading the database.
    This method consumes a lot of database execution power.
    file - The file (in memory) to load database from.
    """
    
    setup_database()
        # Parse the file creating objects for loading database.
    LotoDraw.objects.all().delete()
    ldp = LotoDrawParser()
    ldp.draw_from_file(file)

class LotoDrawParser:
    """
        Knows how to parse a file with lotteries results downloaded from caixa 
        site.
    """
    IDX_DRAW_ID = 0
    IDX_DRAW_DATE = 1
    IDX_DRAW_NUMBER_1 = 2
    IDX_DRAW_NUMBER_2 = 3
    IDX_DRAW_NUMBER_3 = 4
    IDX_DRAW_NUMBER_4 = 5
    IDX_DRAW_NUMBER_5 = 6
    IDX_DRAW_NUMBER_6 = 7
    IDX_DRAW_NUMBER_7 = 8
    IDX_DRAW_NUMBER_8 = 9
    IDX_DRAW_NUMBER_9 = 10
    IDX_DRAW_NUMBER_10 = 11
    IDX_DRAW_NUMBER_11 = 12
    IDX_DRAW_NUMBER_12 = 13
    IDX_DRAW_NUMBER_13 = 14
    IDX_DRAW_NUMBER_14 = 15
    IDX_DRAW_NUMBER_15 = 16
    IDX_TOTAL_COLLECTED = 17
    IDX_TOTAL_WINNERS = 18
    IDX_CITY = 19
    IDX_STATE = 20
    IDX_PRIZE_PER_WINNER = 25
    IDX_PRIZE_FOR_NEXT_DRAW = 30

    def draw_from_file(self, file):
        for encoded_line in file:
            line = encoded_line.decode()
            word_list = line.split(',')

            # Lines beginning with commas are not accepted.
            if line[0] != ',':
                loto_draw = LotoDraw()

                loto_draw.draw_number = \
                        int(word_list[LotoDrawParser.IDX_DRAW_ID])
                dts = strptime(word_list[LotoDrawParser.IDX_DRAW_DATE],
                                       '%d/%m/%Y')
                loto_draw.date = date(dts.tm_year, dts.tm_mon, dts.tm_mday)
                loto_draw.number_1  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_1])
                loto_draw.number_2  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_2])
                loto_draw.number_3  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_3])
                loto_draw.number_4  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_4])
                loto_draw.number_5  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_5])
                loto_draw.number_6  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_6])
                loto_draw.number_7  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_7])
                loto_draw.number_8  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_8])
                loto_draw.number_9  = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_9])
                loto_draw.number_10 = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_10])
                loto_draw.number_11 = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_11])
                loto_draw.number_12 = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_12])
                loto_draw.number_13 = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_13])
                loto_draw.number_14 = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_14])
                loto_draw.number_15 = int(word_list[LotoDrawParser.IDX_DRAW_NUMBER_15])
                loto_draw.total_collected = \
                        Decimal(word_list[LotoDrawParser.IDX_TOTAL_COLLECTED])
                loto_draw.total_winners = int(word_list[LotoDrawParser.IDX_TOTAL_WINNERS])

                if loto_draw.total_winners > 0:
                    loto_draw.prize_per_winner = \
                        Decimal(word_list[LotoDrawParser.IDX_PRIZE_PER_WINNER])
                else:
                    loto_draw.prize_per_winner = 0

                loto_draw.prize_for_next_draw = \
                        Decimal(word_list[LotoDrawParser.IDX_PRIZE_FOR_NEXT_DRAW])
                loto_draw.save()

                if loto_draw.total_winners > 0:
                    ab_state = word_list[LotoDrawParser.IDX_STATE].strip()
                    city_name = word_list[LotoDrawParser.IDX_CITY].strip()
                    city = self.get_city_by_name(city_name, ab_state)
                    win_city = WinningCity()
                    win_city.city = city
                    win_city.differentiator = 1
                    win_city.save()
                    loto_draw.winning_cities.add(win_city)
                    loto_draw.save()
                    
            elif loto_draw and loto_draw.winning_cities:
                ab_state = word_list[LotoDrawParser.IDX_STATE].strip()
                city_name = word_list[LotoDrawParser.IDX_CITY].strip()
                city = self.get_city_by_name(city_name, ab_state)

                diff_factor = (loto_draw.winning_cities
                        .filter(city__name=city.name)
                        .aggregate(Max('differentiator'))['differentiator__max'])
                if diff_factor:
                    sec_win_city = WinningCity()
                    sec_win_city.city = city
                    sec_win_city.differentiator = diff_factor + 1
                    sec_win_city.save()
                    loto_draw.winning_cities.add(sec_win_city)
                else:
                    win_city = WinningCity()
                    win_city.city = city
                    win_city.differentiator = 1
                    win_city.save()
                    loto_draw.winning_cities.add(win_city)
                    loto_draw.save()
    
    def get_city_by_name(self, city_name, state_abbreviation):
        city = None

        if city_name == '':
            city_name = "cidade_" + state_abbreviation
        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            city = City()
            city.name = city_name
            city.state = State.objects.get(abbreviation=state_abbreviation)
            city.save()
        return city

