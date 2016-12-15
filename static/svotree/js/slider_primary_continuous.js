/* Contains variables and actions specific to the continuous version of the slider measure */

var continuous_final_number = 100;

/* Create each slider and attach the necessary event handlers */

var item1_slider = $('#item1').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item1', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item1_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item1', proportional_position_on_slider);
}).data('slider');

var item2_slider = $('#item2').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item2', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item2_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item2', proportional_position_on_slider);
}).data('slider');

var item3_slider = $('#item3').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item3', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item3_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item3', proportional_position_on_slider);
}).data('slider');

var item4_slider = $('#item4').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item4', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item4_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item4', proportional_position_on_slider);
}).data('slider');

var item5_slider = $('#item5').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item5', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item5_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item5', proportional_position_on_slider);
}).data('slider');

var item6_slider = $('#item6').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item6', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item6_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item6', proportional_position_on_slider);
}).data('slider');


/* Update all displayed values for the first time */

update_displayed_values('item1', item1_slider.getValue() / continuous_final_number);
update_displayed_values('item2', item2_slider.getValue() / continuous_final_number);
update_displayed_values('item3', item3_slider.getValue() / continuous_final_number);
update_displayed_values('item4', item4_slider.getValue() / continuous_final_number);
update_displayed_values('item5', item5_slider.getValue() / continuous_final_number);
update_displayed_values('item6', item6_slider.getValue() / continuous_final_number);