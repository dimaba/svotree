/* Contains actions to perform for pages containing primary slider items, not specific to the continuous or discrete
 * version */

/* Register all confirmation button event handlers */

$("#item1_confirm").click(function() {

		$("#item1").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item2_confirm").click(function() {

		$("#item2").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item3_confirm").click(function() {

		$("#item3").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item4_confirm").click(function() {

		$("#item4").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item5_confirm").click(function() {

		$("#item5").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item6_confirm").click(function() {

		$("#item6").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );


/* On submit, check if all choices are confirmed. If not: display error and do not submit */
$("#continue_button").click(function() {
        if (check_all_confirmed(1, 6)) {
            $("#hidden_submit_button").click();
        }
        else {
            $("#confirmation_error").show();
            window.scrollTo(0, 0);
        }
    }
    );

/* Execute on script load */

// Update all start and end values
for (i = 1; i <= 6; i++) {
    update_by_id('item' + i + '_self_start', allocation_bounds['item' + i]['self_left']);
    update_by_id('item' + i + '_self_end', allocation_bounds['item' + i]['self_right']);
    update_by_id('item' + i + '_other_start', allocation_bounds['item' + i]['other_left']);
    update_by_id('item' + i + '_other_end', allocation_bounds['item' + i]['other_right']);
}