""""
Functions to evaluate input from the nine-item triple dominance measure and calculate the resulting SVO values.
"""

decisions = [
    {'number': 1, 'A': {'self': 80, 'other': 0}, 'B': {'self': 92, 'other': 40},
     'C': {'self': 80, 'other': 80}},
    {'number': 2, 'A': {'self': 94, 'other': 44}, 'B': {'self': 84, 'other': 84},
     'C': {'self': 84, 'other': 4}},
    {'number': 3, 'A': {'self': 88, 'other': 88}, 'B': {'self': 88, 'other': 4},
     'C': {'self': 100, 'other': 48}},
    {'number': 4, 'A': {'self': 84, 'other': 4}, 'B': {'self': 94, 'other': 44},
     'C': {'self': 82, 'other': 82}},
    {'number': 5, 'A': {'self': 96, 'other': 44}, 'B': {'self': 84, 'other': 84},
     'C': {'self': 82, 'other': 2}},
    {'number': 6, 'A': {'self': 84, 'other': 84}, 'B': {'self': 84, 'other': 4},
     'C': {'self': 98, 'other': 44}},
    {'number': 7, 'A': {'self': 86, 'other': 86}, 'B': {'self': 94, 'other': 44},
     'C': {'self': 86, 'other': 6}},
    {'number': 8, 'A': {'self': 94, 'other': 44}, 'B': {'self': 84, 'other': 4},
     'C': {'self': 84, 'other': 84}},
    {'number': 9, 'A': {'self': 80, 'other': 4}, 'B': {'self': 82, 'other': 82},
     'C': {'self': 92, 'other': 44}},

]


decisions_by_type = {
    1: {'A': "Competitive", 'B': "Individualistic", 'C': "Prosocial"},
    2: {'A': "Individualistic", 'B': "Prosocial", 'C': "Competitive"},
    3: {'A': "Prosocial", 'B': "Competitive", 'C': "Individualistic"},
    4: {'A': "Competitive", 'B': "Individualistic", 'C': "Prosocial"},
    5: {'A': "Individualistic", 'B': "Prosocial", 'C': "Competitive"},
    6: {'A': "Prosocial", 'B': "Competitive", 'C': "Individualistic"},
    7: {'A': "Prosocial", 'B': "Individualistic", 'C': "Competitive"},
    8: {'A': "Individualistic", 'B': "Competitive", 'C': "Prosocial"},
    9: {'A': "Competitive", 'B': "Prosocial", 'C': "Individualistic"},
}


def decision_corresponding_type(item, choice):
    """
    Get the SVO type which corresponds to the choice a person made on a given item of the Nine-Item Triple Dominance
    Measure.

    params: The choice taken (A, B or C) and the item on which the choice was taken
    returns: The SVO type corresponding to this choice for this item
    effects: None
    """

    return decisions_by_type[item][choice]


def count_decisions_of_type(type_to_count, decisions_taken):
    """
    Count the number of choices corresponding to a given SVO type a person selected,
    across all items of the Nine-Item Triple Dominance Measure.

    params: The type to look for (Prosocial, Individualistic or Competitive) and a dictionary of decisions taken
        with the form decision_number: decision_value (which can be A, B or C)
    returns: The number of choices of the given type selected by this player
    effects: None
    """

    decision_corresponding_types = [decision_corresponding_type(item_number, decisions_taken[item_number]) for item_number in range(1, 10)]

    return decision_corresponding_types.count(type_to_count)


def svo_type(decisions_taken):
    """
    Determine the SVO type of a person selected based on the Nine-Item Triple Dominance Measure.

    params: A dictionary of decisions taken with the form decision_number: decision_value (which can be A, B or C)
    returns: The SVO type corresponding to this pattern of decisions
    effects: None
    """

    decisions_prosocial = count_decisions_of_type("Prosocial", decisions_taken)
    decisions_individualistic = count_decisions_of_type("Individualistic", decisions_taken)
    decisions_competitive = count_decisions_of_type("Competitive", decisions_taken)

    if decisions_prosocial >= 6:
        return "Prosocial"
    elif decisions_individualistic >= 6:
        return "Individualistic"
    elif decisions_competitive >= 6:
        return "Competitive"
    else:
        return "Unclassified/Mixed"
