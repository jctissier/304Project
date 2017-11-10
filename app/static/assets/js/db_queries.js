/**
 *  JS functions for all AJAX queries
 */

// $(document).ready(function() {
//
//     $.ajax({
//         type: 'GET',
//         url: '/recent_entries'
//     })
//             .done(function (response) {
//                 console.log(response);
//                 $('#last_5_days_entries').html(recent_entries_table(response));
//
//             });
// });


/**
 * SELECT queries
 */

function select_athlete(){
    $.ajax({
        type: 'GET',
        url: '/select_athlete'
    })
            .done(function (response) {
                console.log(response);
                $('#select_table_insertion').html(select_athlete_table(response));
            });
}

function select_athlete_table(jsonData){
    var html = '';
    jsonData = jsonData['entries'];

    for (var key in jsonData) {
        if (jsonData.hasOwnProperty(key)) {

            html += '<tr>' +
                        '<td>' + jsonData[key][0].project.replace("Inventory Management Database", "Inventory Management") + '</td>' +
                        '<td>' + jsonData[key][0].start.replace("GMT", "") + '</td>' +
                        '<td>' + jsonData[key][0].end.replace("GMT", "") + '</td>' +
                        '<td>' + jsonData[key][0].duration + '</td>' +
                        '<td>' + jsonData[key][0].notes + '</td>' +
                    '</tr>';
        }
    }

return html;
}

/**
 * OTHER queries
 */