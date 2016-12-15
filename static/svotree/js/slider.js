/* Contains functions used by all slider measure pages (such as getting allocations, updating the slider
 * and values etc). Also contains the allocation boundaries for all slider items (primary and secondary). */

/* Functions */

function get_allocation(left_bound, right_bound, proportional_location_on_slider) {
    /* Calculate the selected allocation based on the chosen position
     * along the slider axis. Returns the nearest integer. */

    var range = right_bound - left_bound;

    var allocation_exact = left_bound + (proportional_location_on_slider * range);

    return Math.round(allocation_exact);
}

function tooltip_text(item, proportional_position_on_slider) {
    /* Generate text to apply to the tooltip which appears over the slider when it is hovered over. */
    var allocation_self = get_allocation(allocation_bounds[item]['self_left'], allocation_bounds[item]['self_right'], proportional_position_on_slider);
    var allocation_other = get_allocation(allocation_bounds[item]['other_left'], allocation_bounds[item]['other_right'], proportional_position_on_slider);
    return 'You: ' + allocation_self + ', Other: ' + allocation_other;
}

function update_displayed_values(item_id, proportional_position_on_slider) {
    /* Update the displayed values for selected self/other allocation based on the
     * chosen position along the slider axis.  */

    var self_value_id = item_id + "_self";
    var other_value_id = item_id + "_other";

    var allocation_self = get_allocation(allocation_bounds[item_id]['self_left'], allocation_bounds[item_id]['self_right'], proportional_position_on_slider);
    var allocation_other = get_allocation(allocation_bounds[item_id]['other_left'], allocation_bounds[item_id]['other_right'], proportional_position_on_slider);

    update_by_id(self_value_id, allocation_self)
    update_by_id(other_value_id, allocation_other)
}

function check_all_confirmed(first_item_number, last_item_number) {
    /* Check that the allocations of the items from first_item_number to last_item_number have been confirmed */
    var number_confirmed = 0
    for (i = first_item_number; i <= last_item_number; i++) {
        if ($("#item" + i + "_confirm").val() === "True") {
            number_confirmed++;
        }
    }

    return number_confirmed === (1 + last_item_number - first_item_number);
}

/* Global variables */

var allocation_bounds = {
    /* Left and right bounds for what self and other can receive for each item */
    item1: {self_left: 85, self_right: 85, other_left: 85, other_right: 15},
    item2: {self_left: 85, self_right: 100, other_left: 15, other_right: 50},
    item3: {self_left: 50, self_right: 85, other_left: 100, other_right: 85},
    item4: {self_left: 50, self_right: 85, other_left: 100, other_right: 15},
    item5: {self_left: 100, self_right: 50, other_left: 50, other_right: 100},
    item6: {self_left: 100, self_right: 85, other_left: 50, other_right: 85},
};


/* Execute on script load */