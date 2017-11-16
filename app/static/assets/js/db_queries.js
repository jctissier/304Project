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
 * Globals
 */
var select_options_athlete = "";
var select_options_team = "";
var select_options_coach = "";
var insert_options_athlete = "";
var insert_options_team = "";

var dropdown_options = {
    "select_options_athlete" :select_options_athlete,
    "select_options_team": select_options_team,
    "select_options_coach": select_options_coach,
    "insert_options_athlete": insert_options_athlete,
    "insert_options_team": insert_options_team
};


/**
 * Helper functions
 */

function isEqual(myVar, myVal){
    return myVar === myVal;
}

function add_dropdown_icon(el_id, prefix){
    $('#' + prefix + '-' + el_id).append(
        '<i id="' + el_id + '" class="material-icons" style="font-size: 15px;float: right;color: green;font-weight: bolder;">done</i>'
    );
}

function dropdown_check(tName, el_id){
    // TODO - how to add and remove checkmark
    uncheck_others(el_id);

    if (dropdown_options[el_id] == ""){
        console.log('Empty');
        dropdown_options[el_id] = el_id;
        $('#' + el_id).append(
            '<i id="check_' + el_id + '" class="material-icons" style="font-size: 15px;float: right;color: green;font-weight: bolder;">done</i>'
        );
    }
    else {
        console.log('Exists');
        $('#check_' + el_id).remove();
        dropdown_options[el_id] = "";
    }

    // map_to_functions(tName, el_id);

}

function uncheck_others(el_id){
    var keys = Object.keys(dropdown_options);
    var prefix = el_id.split('_')[0];
    console.log(keys);
    console.log(prefix);

    for (var i=0; i < keys.length; i++){
        // TODO - add rest of function mapping
        console.log(prefix.indexOf('insert'));
        if (prefix.indexOf('insert') !== -1 && keys[i] !== el_id){
            dropdown_options[keys[i]] = "";
            console.log('1#check_' + dropdown_options[keys[i]]);
            $('#check_' + dropdown_options[keys[i]]).remove();
        }
        else if (prefix.indexOf('select') !== -1 && dropdown_options[keys[i]] !== el_id){
            dropdown_options[keys[i]] = "";
            $('#check_' + dropdown_options[keys[i]]).remove();
        }
    }
}

function map_to_functions(tName, el_id){
    if (el_id.indexOf('insert_') !== -1){
        insert_options(tName);
    }
    else if (el_id.indexOf('select_') !== -1){
        select_queries(tName);
    }
    // TODO - add rest of function mapping

}


/**
 * View DB Tables
 */
function view_tables(tname){
    $.ajax({
        type: 'GET',
        url: '/db_tables',
        data: {
            table_name: tname
        }
    })
            .done(function (response) {
                demo.showNotification("Viewing all rows in DB Table: " + tname, "danger");
                $('#response-json').text(JSON.stringify(response.entries, undefined, 4));
                $('#db_table_insertion_headers').html(db_table_headers(response.headers));
                $('#db_table_insertion_body').html(db_table_vars(response.entries));
            });
}

function db_table_vars(jsonData, tname){
    var tbody = '';
    for (var key in jsonData) {
        if (jsonData.hasOwnProperty(key)) {
            tbody += '<tr>';

            for (var i=0; i<jsonData[key].length; i++){
                tbody += '<td>' + jsonData[key][i] + '</td>';
            }
            tbody += '<tr>';
        }
    }
    print(tbody);
    return tbody + '</tr>';
}

function get_db_table_keys(jsonData, loop){
    var a_html = "";
    for (var k=0; k<a_keys.length; k++){
        a_html += '<td>' + jsonData[loop][0][a_keys[k]] + '</td>';
    }
    return a_html;
}

function db_table_headers(jsonData) {
    var headers = '<tr>';
    for (var key in jsonData){
        headers += '<th>' + jsonData[key] + '</th>';
    }

    return headers + '</tr>';
}



/**
 * SELECT queries
 */

function hide_select(){
    $('#select-content').hide();        // main content
    $('#select_query_athlete').hide();
    $('#select_query_coach').hide();
    $('#select_query_team').hide();
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
                $('#response-json').text(JSON.stringify(response.entries, undefined, 4));
                $('#select_table_insertion').html(select_table_vars(response, tname));
            });
}

function select_table_vars(jsonData, tname){
    jsonData = jsonData['entries'];

    var html = get_select_table_headers(tname) + '<tbody>';
    for (var key in jsonData) {
        if (jsonData.hasOwnProperty(key)) {
            html += '<tr>' + get_select_table_keys(jsonData, key, tname) + '</tr>';
        }
    }
    html += '</tbody>';

    return html;
}

function get_select_table_keys(jsonData, loop, tname){
    var a_keys;
    if (isEqual(tname, "Athlete")){a_keys = ["name", "countryID", "dob", "placeOfBirth", "salary", "status", "goals", "assists", "wins", "losses"]}
    else if (isEqual(tname, "Team")){a_keys = ["name", "location", "dateCreated", "goals", "assists", "wins", "losses"]}
    else if (isEqual(tname, "Coach")){a_keys = ["name", "salary", "dob", "status", "placeOfBirth", "countryID"]}

    var a_html = "";
    for (var k=0; k<a_keys.length; k++){
        a_html += '<td>' + jsonData[loop][0][a_keys[k]] + '</td>';
    }
    return a_html;
}

function get_select_table_headers(tname){
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
                    '<th>Team ID</th>' +
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
 * INSERT queries
 */
var insert_aName = "";
var insert_aStatus = "";
var insert_tName= "";
var insert_tLocation = "";

function insert_dropdown(val, type){
    if (isEqual(type, "aName")) {
        if (insert_aName !== "") {
            $('#' + insert_aName).remove();
        }
        insert_aName = val;
    }
    else if (isEqual(type, "aStatus")){
        if (insert_aStatus !== "") {
            $('#' + insert_aStatus).remove();
        }
        insert_aStatus = val;
    }
    else if (isEqual(type, "tName")){
        if (insert_tName !== "") {
            $('#' + insert_tName).remove();
        }
        insert_tName = val;
    }
    else if (isEqual(type, "tLocation")){
        if (insert_tLocation !== "") {
            $('#' + insert_tLocation).remove();
        }
        insert_tLocation = val;
    }
    add_dropdown_icon(val, "insert");
}

function hide_insert(tname){
    if (isEqual(tname, "Athlete")) {
        $('#insert_query_athlete_demo').hide();
        $('#insert-athlete-content').show();
    }
    else if (isEqual(tname, "Team")){
        $('#insert_query_team_demo').hide();
        $('#insert-team-content').show();
    }
}

function check_dropdown_vals_insert(tname){
    if (isEqual(tname, "Athlete")){
        if (isEqual(insert_aName, "")){
            demo.showNotification("Athlete Name has not been selected", "info");
            return false;
        }
        if (isEqual(insert_aStatus, "")){
            demo.showNotification("Athlete Status has not been selected", "info");
            return false;
        }
        return true;
    }
    else if (isEqual(tname, "Team")){
        if (isEqual(insert_tName, "")){
            demo.showNotification("Team Name has not been selected", "info");
            return false;
        }
        if (isEqual(insert_tLocation, "")){
            demo.showNotification("Team Location has not been selected", "info");
            return false;
        }
        return true;
    }
}

function insert_queries(tname){
    var isFilledIn = check_dropdown_vals_insert(tname);
    if (isFilledIn) {

        hide_insert(tname);           // todo

        $.ajax({
            type: 'POST',
            url: '/insert_query',
            data: {
                table_name: tname,
                a_name: insert_aName,
                a_status: insert_aStatus,
                t_name: insert_tName,
                t_location: insert_tLocation
            }
        })
            .done(function (response) {
                demo.showNotification("INSERT query completed", "danger");
                $('#insert-content').show();
                $('#response-json').text(JSON.stringify(response, undefined, 4));
                if (isEqual(tname, "Athlete")){
                    $('#insert_table_insertion_athlete').html(insert_table_vars(response.last_5_rows, tname));
                }
                else{
                    $('#insert_table_insertion_team').html(insert_table_vars(response.last_5_rows, tname));
                }

            });
    }
}

function insert_options(tname){
    if (isEqual(tname, "Athlete")){
        $('#insert-team-options').hide();
        $('#insert-team-content').hide();
        $('#insert-athlete-options').show();

    }
    else if (isEqual(tname, "Team")){
        $('#insert-athlete-options').hide();
        $('#insert-athlete-content').hide();
        $('#insert-team-options').show();
    }
}

function insert_table_vars(jsonData, tname){
    var html = get_insert_table_headers(tname) + '<tbody>';

    for (var k=0; k<jsonData.length; k++){
        html += '<tr>';
        for (var i=0; i<jsonData[k].length; i++) {
            html += '<td>' + jsonData[k][i] + '</td>';
        }
        html += '</tr>';
    }
    html += '</tbody>';

    return html;
}

function get_insert_table_headers(tname){
    if (isEqual(tname, "Athlete")) {
        return '<thead class="text-danger">' +
                    '<th>ID</th>' +
                    '<th>Salary</th>' +
                    '<th>Name</th>' +
                    '<th>Date of Birth</th>' +
                    '<th>Status</th>' +
                    '<th>Place of Birth</th>' +
                    '<th>Country ID</th>' +
                    '<th>Goals</th>' +
                    '<th>Assists</th>' +
                    '<th>Wins</th>' +
                    '<th>Losses</th>' +
                '</thead>';
    }
    else if (isEqual(tname, "Team")){
        return '<thead class="text-danger">' +
                    '<th>Team ID</th>' +
                    '<th>Location</th>' +
                    '<th>Date Created</th>' +
                    '<th>Goals</th>' +
                    '<th>Assists</th>' +
                    '<th>Wins</th>' +
                    '<th>Losses</th>' +
                '</thead>';
    }
}


/**
 * DELETE queries
 *      - delete stadium
 *      - delete team
 */
var delete_sName = "";
var delete_sLocation = "";          // This needs to be set based on Stadium Name
var delete_teamID = "";


function delete_options(tname){
    if (isEqual(tname, "Stadium")){
        $('#delete-team-options').hide();
        $('#delete-team-content').hide();
        $('#delete-stadium-options').show();

    }
    else if (isEqual(tname, "Team")){
        $('#delete-stadium-options').hide();
        $('#delete-stadium-content').hide();
        $('#delete-team-options').show();
    }
}

function delete_dropdown(val, type){
    if (isEqual(type, "sName")) {
        if (delete_sName !== "") {
            $('#' + delete_sName).remove();
        }
        val = val.replace(' ', '-');
        delete_sName = val;
        if (delete_sName === "Allianz-Arena"){
            delete_sLocation = "Munich, Germany"
        }
        else if (delete_sName === "Anfield"){
            delete_sLocation = "Liverpool, England"
        }
        else if (delete_sName === "Camp-Nou"){
            delete_sLocation = "Barcelona, Spain"
        }
    }
    else if (isEqual(type, "tName")){
        if (delete_teamID !== "") {
            $('#' + delete_teamID).remove();
        }
        delete_teamID = val;
    }
    add_dropdown_icon(val, "delete");
}

function check_dropdown_vals_delete(tname){
    if (isEqual(tname, "Stadium")){
        if (isEqual(delete_sName, "")){
            demo.showNotification("Stadium Name has not been selected", "info");
            return false;
        }
    }
    else if (isEqual(tname, "Team")){
        if (isEqual(delete_teamID, "")){
            demo.showNotification("Team Name has not been selected", "info");
            return false;
        }
    }
    return true;
}

function delete_queries(tname){
    var isFilledIn = check_dropdown_vals_delete(tname);
    if (isFilledIn) {

        hide_delete(tname);           // todo

        $.ajax({
            type: 'POST',
            url: '/delete_query',
            data: {
                table_name: tname,
                s_name: delete_sName,
                s_location: delete_sLocation,
                t_name: delete_teamID
            }
        })
            .done(function (response) {
                demo.showNotification("DELETE query completed", "danger");
                $('#delete-content').show();
                $('#response-json').text(JSON.stringify(response, undefined, 4));
                if (isEqual(tname, "Stadium")){
                    $('#delete_table_insertion_stadium').html(delete_table_vars(response.last_5_rows, tname));
                }
                else{
                    $('#delete_table_insertion_team').html(delete_table_vars(response.last_5_rows, tname));
                }

            });
    }
}

function delete_table_vars(jsonData, tname){
    var html = get_delete_table_headers(tname) + '<tbody>';

    for (var k=0; k<jsonData.length; k++){
        html += '<tr>';
        for (var i=0; i<jsonData[k].length; i++) {
            html += '<td>' + jsonData[k][i] + '</td>';
        }
        html += '</tr>';
    }
    html += '</tbody>';

    return html;
}

function get_delete_table_headers(tname){
    // TODO - fix this when
    if (isEqual(tname, "Stadium")) {
        return '<thead class="text-danger">' +
                    '<th>Name</th>' +
                    '<th>Location</th>' +
                '</thead>';
    }
    else if (isEqual(tname, "Team")){
        return '<thead class="text-danger">' +
                    '<th>ID</th>' +
                    '<th>Team ID</th>' +
                    '<th>Location</th>' +
                '</thead>';
    }
}

function hide_delete(tname){
    if (isEqual(tname, "Stadium")) {
        $('#delete_query_stadium_demo').hide();
        $('#delete-stadium-content').show();
    }
    else if (isEqual(tname, "Team")){
        $('#delete_query_team_demo').hide();
        $('#delete-team-content').show();
    }
}