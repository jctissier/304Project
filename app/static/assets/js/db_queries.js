/**
 * Globals
 */
var select_table = "";



/**
 *  JS functions for all AJAX queries
 */
$(document).ready(function() {

    demo = {
        showNotification: function (message, color) {
            $.notify({
                icon: "notifications",
                message: message

            }, {
                type: color,
                timer: 4000,
                placement: {
                    from: "top",
                    align: "right"
                }
            });
        }
    }

});



/**
 * SELECT queries
 */

function hide_select(){
    $('#select-content').hide();        // main content
    $('#select_query_athlete').hide();
    $('#select_query_coach').hide();
    $('#select_query_team').hide();
}

function show_sql_code(tname){
    if (tname === "Athlete"){
        $('#select_query_athlete').show();
    }
    else if (tname === "Team"){
        $('#select_query_team').show();
    }
    else if (tname === "Coach"){
        $('#select_query_coach').show();
    }
}

function select_queries(tname){
    hide_select();
    $.ajax({
        type: 'POST',
        url: '/select_query',
        data: {
            table_name: tname
        }
    })
            .done(function (response) {
                demo.showNotification("SELECT query completed", "danger");
                $('#select-content').show();
                show_sql_code(tname);
                $('#select-response-json').text(JSON.stringify(response.entries, undefined, 4));
                $('#select_table_insertion').html(select_table_vars(response, tname));
            });
}

function select_table_vars(jsonData, tname){
    jsonData = jsonData['entries'];

    var html = get_table_headers(tname) + '<tbody>';
    for (var key in jsonData) {
        if (jsonData.hasOwnProperty(key)) {
            html += '<tr>' + get_table_keys(jsonData, key, tname) + '</tr>';
        }
    }
    html += '</tbody>';

    return html;
}

function get_table_keys(jsonData, loop, tname){
    var a_keys;
    if (tname === "Athlete"){
        a_keys = ["name", "countryID", "dob", "placeOfBirth", "salary", "status", "goals", "assists", "wins", "losses"]
    }
    else if (tname === "Team"){
        a_keys = ["name", "location", "dateCreated", "goals", "assists", "wins", "losses"]
    }
    else if (tname === "Coach"){
        a_keys = ["name", "salary", "dob", "status", "placeOfBirth", "countryID"]
    }

    var a_html = "";
    for (var k=0; k<a_keys.length; k++){
        a_html += '<td>' + jsonData[loop][0][a_keys[k]] + '</td>';
    }
    return a_html;
}

function get_table_headers(tname){
    if (tname === "Athlete") {
        return '<thead class="text-danger">' +
                    '<th>Name</th>' +
                    '<th>Country</th>' +
                    '<th>Date of Birth</th>' +
                    '<th>Place of Birth</th>' +
                    '<th>Salary</th>' +
                    '<th>Status</th>' +
                    '<th>Goals</th>' +
                    '<th>Assists</th>' +
                    '<th>Wins</th>' +
                    '<th>Losses</th>' +
                '</thead>';
    }
    else if (tname === "Team"){
        return '<thead class="text-danger">' +
                    '<th>Name</th>' +
                    '<th>Location</th>' +
                    '<th>Date Created</th>' +
                    '<th>Goals</th>' +
                    '<th>Assists</th>' +
                    '<th>Wins</th>' +
                    '<th>Losses</th>' +
                '</thead>';
    }
    else if (tname === "Coach"){
        return '<thead class="text-danger">' +
                    '<th>Name</th>' +
                    '<th>Salary</th>' +
                    '<th>Date of Birth</th>' +
                    '<th>Place of Birth</th>' +
                    '<th>Status</th>' +
                    '<th>CountryID</th>' +
                '</thead>';
    }
}


/**
 * OTHER queries
 */