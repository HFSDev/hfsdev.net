from lotteries.models import LotoDraw
from datetime import date
from time import strptime
from decimal import Decimal

def load_data_from_file(file):
    """
    Deletes all draws and its numbers for reloading the database.
    This method consumes a lot of database execution power.
    file - The file (in memory) to load database from.
    """
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
                loto_draw.number_1 = int(word_list[IDX_DRAW_NUMBER_1])
                loto_draw.number_2 = int(word_list[IDX_DRAW_NUMBER_2])
                loto_draw.number_3 = int(word_list[IDX_DRAW_NUMBER_3])
                loto_draw.number_4 = int(word_list[IDX_DRAW_NUMBER_3])
                loto_draw.number_5 = int(word_list[IDX_DRAW_NUMBER_5])
                loto_draw.number_6 = int(word_list[IDX_DRAW_NUMBER_6])
                loto_draw.number_7 = int(word_list[IDX_DRAW_NUMBER_7])
                loto_draw.number_8 = int(word_list[IDX_DRAW_NUMBER_8])
                loto_draw.number_9 = int(word_list[IDX_DRAW_NUMBER_9])
                loto_draw.number_10 = int(word_list[IDX_DRAW_NUMBER_10])
                loto_draw.number_11 = int(word_list[IDX_DRAW_NUMBER_11])
                loto_draw.number_12 = int(word_list[IDX_DRAW_NUMBER_12])
                loto_draw.number_13 = int(word_list[IDX_DRAW_NUMBER_12])
                loto_draw.number_14 = int(word_list[IDX_DRAW_NUMBER_13])
                loto_draw.number_15 = int(word_list[IDX_DRAW_NUMBER_14])
                loto_draw.total_collected = \
                        Decimal(word_list[IDX_TOTAL_COLLECTED])
                loto_draw.total_winners = int(word_list[IDX_TOTAL_WINNERS])

                if loto_draw.total_winners > 0:
                    loto_draw.prize_per_winner = \
                        Decimal(word_list[IDX_PRIZE_PER_WINNER])
                else:
                    loto_draw.prize_per_winner = 0

                loto_draw.prize_for_next_draw = \
                        Decimal(word_list[IDX_PRIZE_FOR_NEXT_DRAW])

                ab_state = word_list[IDX_STATE]
                city_name = word_list[IDX_CITY]
                if city_name and len(city_name) > 0:
                    city = City.objects.get(name=city_name)
                    if not city:
                        city = City()
                        city.name = city_name
                        city.state = State.objects.get(abbreviation=ab_state)
                        city.save()
                    loto_draw.winning_cities.add(city)
                loto_draw.save()

            elif draw and draw.winning_cities:
                ab_state = word_list[IDX_STATE]
                city_name = word_list[LotoDrawParser.IDX_CITY]
                city = City.oebjects.get(name=city_name)
                if not city:
                    city = City()
                    city.name = city_name
                    city.state = State.objects.get(abbreviation=ab_state)
                    city.save()
                loto_draw.winning_cities.add(city)
                loto_draw.save()






