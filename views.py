from . import models
from ._builtin import Page, WaitPage
from .functions import slider
from otree.api import Currency as c, currency_range
from .models import Constants


class SliderPrimaryDiscrete(Page):

    form_model = models.Player
    form_fields = ['slider1',
                   'slider2',
                   'slider3',
                   'slider4',
                   'slider5',
                   'slider6',
                ]

    def vars_for_template(self):
        return {'slider_items': [1, 2, 3, 4, 5, 6]}

    def before_next_page(self):
        chosen_values = {
            'item1': self.player.slider1,
            'item2': self.player.slider2,
            'item3': self.player.slider3,
            'item4': self.player.slider4,
            'item5': self.player.slider5,
            'item6': self.player.slider6
        }
        mean_allocations = slider.mean_allocations(chosen_values, discrete=True)
        svo_slider_angle = slider.svo_angle(mean_allocations['self'], mean_allocations['other'])
        self.player.slider_angle = svo_slider_angle


class SliderPrimaryContinuous(Page):

    form_model = models.Player
    form_fields = ['slider1',
                   'slider2',
                   'slider3',
                   'slider4',
                   'slider5',
                   'slider6',
                ]

    def vars_for_template(self):
        return {'slider_items': [1, 2, 3, 4, 5, 6]}

    def before_next_page(self):
        chosen_values = {
            'item1': self.player.slider1,
            'item2': self.player.slider2,
            'item3': self.player.slider3,
            'item4': self.player.slider4,
            'item5': self.player.slider5,
            'item6': self.player.slider6
        }
        mean_allocations = slider.mean_allocations(chosen_values, discrete=False)
        svo_slider_angle = slider.svo_angle(mean_allocations['self'], mean_allocations['other'])
        self.player.slider_angle = svo_slider_angle


class NineItemTDM(Page):

    #form

    def vars_for_template(self):
        decisions = [
            {'number': 1, 'optionA': 'You: 80 - Other: 0', 'optionB': 'You: 92 - Other: 40', 'optionC': 'You: 80 - Other: 80'},
        ]

        return {'decisions': decisions}

class DebugDisplayPage(Page):

    def vars_for_template(self):
        return {'angle': self.player.slider_angle}

page_sequence = [
    NineItemTDM
]
