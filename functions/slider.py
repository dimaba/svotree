""""
Functions to evaluate input from the slider measure and calculate the resulting SVO values.
"""

import math

items = {
    'item1': {'self_left': 85, 'self_right': 85, 'other_left': 85, 'other_right': 15},
    'item2': {'self_left': 85, 'self_right': 100, 'other_left': 15, 'other_right': 50},
    'item3': {'self_left': 50, 'self_right': 85, 'other_left': 100, 'other_right': 85},
    'item4': {'self_left': 50, 'self_right': 85, 'other_left': 100, 'other_right': 15},
    'item5': {'self_left': 100, 'self_right': 50, 'other_left': 50, 'other_right': 100},
    'item6': {'self_left': 100, 'self_right': 85, 'other_left': 50, 'other_right': 85},
             }


def allocation(item, proportional_position_slider):
    """
    Calculate the allocation to self and other which corresponds to a particular position on
    the slider for a specific item.

    params: Chosen position on slider where 0 = left-most and 1 = right-most position possible
    returns: Allocation for self and other corresponding to this position, as dict
    effects: None
    """

    self_range = items[item]['self_right'] - items[item]['self_left']
    self_allocation_exact = items[item]['self_left'] + (self_range * proportional_position_slider)

    other_range = items[item]['other_right'] - items[item]['other_left']
    other_allocation_exact = items[item]['other_left'] + (other_range * proportional_position_slider)

    return {'self': round(self_allocation_exact), 'other': round(other_allocation_exact)}


def proportional_position(value, min_value, max_value):
    """
    Calculate the proportional representation of a position on a given scale.

    params: Value (position on the scale), minimum value (lowest possible value on the scale) and maximum value
    (highest possible value on the scale).
    returns: Proportional position (0 is leftmost, 1 is rightmost)
    effects: None
    """

    return (value - min_value) / (max_value - min_value)


def proportional_position_discrete(value):
    """
    Calculate the proportional representation of a position on the discrete version of the slider.

    params: Value (position on the scale) chosen
    returns: This function calls proportional_position() and returns the result
    effects: None
    """

    return proportional_position(value, 1, 9)


def proportional_position_continuous(value):
    """
    Calculate the proportional representation of a position on the continuous version of the slider.

    params: Value (position on the scale) chosen
    returns: This function calls proportional_position() and returns the result
    effects: None
    """

    return proportional_position(value, 0, 100)


def mean_allocations(chosen_values, discrete):
    """
    Calculate the mean allocations to self and other based on all chosen values on a given group of slider items.

    params: the values must be passed as a dictionary with the structure key = item+number, value = chosen value on
        that item
    returns: A dictionary of mean allocations to self and other
    effects: None
    """

    total_allocation_self = 0
    total_allocation_other = 0

    for item, value in chosen_values.items():
        if discrete:
            chosen_allocation = allocation(item, proportional_position_discrete(value))
        else:
            chosen_allocation = allocation(item, proportional_position_continuous(value))

        allocation_to_self = chosen_allocation['self']
        allocation_to_other = chosen_allocation['other']

        total_allocation_self += allocation_to_self
        total_allocation_other += allocation_to_other

    mean_allocation_self = total_allocation_self / len(chosen_values)
    mean_allocation_other = total_allocation_other / len(chosen_values)

    return {'self': mean_allocation_self, 'other': mean_allocation_other}


def svo_angle(mean_allocation_self, mean_allocation_other):
    """
    Calculate a person's social value orientation angle (based on the slider measure).

    params: A mean allocation to self and a mean allocation to other, based on the six primary items of the SVO slider
    returns: The person's social value orientation angle
    effects: None
    """

    # With the default values of the slider measure, the origin is at 0,0 but the center of the circle is at 50,50
    # By subtracting 50 from both mean allocations we compute the angle from the center of the circle
    return math.degrees(math.atan2(mean_allocation_other - 50, mean_allocation_self - 50))
