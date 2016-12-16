from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'svotree'
    players_per_group = None
    num_rounds = 1

    instructions_slider = 'svotree/SliderInstructions.html'
    instructions_9tdm = 'svotree/NineItemTDMInstructions.html'


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
    slider_classification = models.CharField()

    nine_item_tdm_1 = models.CharField()
    nine_item_tdm_2 = models.CharField()
    nine_item_tdm_3 = models.CharField()
    nine_item_tdm_4 = models.CharField()
    nine_item_tdm_5 = models.CharField()
    nine_item_tdm_6 = models.CharField()
    nine_item_tdm_7 = models.CharField()
    nine_item_tdm_8 = models.CharField()
    nine_item_tdm_9 = models.CharField()
    nine_item_tdm_prosocial = models.IntegerField()
    nine_item_tdm_individualistic = models.IntegerField()
    nine_item_tdm_competitive = models.IntegerField()
    nine_item_tdm_classification = models.CharField()
