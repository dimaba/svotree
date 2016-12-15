/* Contains general functions accessible by all pages */

function update_by_id(element_id, value_to_insert) {

    var value = document.getElementById(element_id);

    value.innerHTML = value_to_insert;

}