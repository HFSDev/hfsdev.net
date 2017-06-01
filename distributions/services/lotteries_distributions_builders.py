from lotteries.models import LotoDraw
from distributions.models import LotoDistribution
from django.db.models import Max

class LotoDrawDistributionBuilder:
    '''
    Provides methods for building distributions on Lotofacil game and 
    interacting with LotoDistribution objects.
    '''
    def get_last_distribution(self):
        '''
        Checks if the database has already saved the last distribution, if it
        hasn't, builds a distribution with all objects that are available from
        Lotofacil games. If database contains the last distribution, returns it.
        '''
        max_draw_analysed = (LotoDraw.objects.all()
                .aggregate(Max('draw_number'))['draw_number__max'])
        if (LotoDistribution.objects
                .filter(draw_marker = max_draw_analysed).exists()):
        # If the last lotodraw in database was already analysed, than there's
        # nothing else to do, just return the distribution.
            return (LotoDistribution.objects
                    .filter(draw_marker=max_draw_analysed)[0])

        # Create empty distribution in a list form.
        dist = []
        for i in range(0, 25):
            dist.insert(i, 0)

        for draw in LotoDraw.objects.all():
            for i in range(1,16):
                # for each number (number_1, number_2, etc), increment the count
                exec("dist[draw.number_"+str(i)+" - 1] += 1")

        distribution = LotoDistribution()
        distribution.draw_marker = max_draw_analysed
        for i in range(1, 26):
            exec ("distribution.count_number_"+str(i)+ " = dist["+str(i)+"-1]")

        return distribution

    def update_with_last_distribution(self):
        dist = get_last_distribution()
        dist.save()