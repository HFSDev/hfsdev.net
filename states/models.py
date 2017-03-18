from django.db import models

class Region(models.Model):
    """
    Defines a brazilian region. This is open to create new regions
    as of north of northeast.
    """
    abbreviation = models.CharField(max_length=2)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.abbreviation

class State(models.Model):
    """
    Defines a brazilian state. This is open to create new states.
    """
    abbreviation = models.CharField(max_length=2)
    name = models.CharField(max_length=32)
    region = models.ForeignKey(Region)

    def __str__(self):
        return "[%s - %s]" % (self.abbreviation, self.name)

class City(models.Model):
    """
    Defines a brazilian city.
    """
    name = models.CharField(max_length=64)
    state = models.ForeignKey(State)
