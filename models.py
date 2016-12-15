from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'svotree'
    players_per_group = None
    num_rounds = 1

    instructions_slider = 'svotree/slider/SliderInstructions.html'
    instructions_9tdm = 'svotree/9tdm/NineItemTDMInstructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, to be implemented later """
        self.payoff = 0

    slider1 = models.FloatField()
    slider2 = models.FloatField()
    slider3 = models.FloatField()
    slider4 = models.FloatField()
    slider5 = models.FloatField()
    slider6 = models.FloatField()

    slider_angle = models.DecimalField(decimal_places=2, max_digits=5)
