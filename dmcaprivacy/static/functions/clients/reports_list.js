var minDate, maxDate;
// Custom filtering function which will search data in column four between two values
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = minDate.val();
        var max = maxDate.val();
        var date = new Date( data[4] );

        if (
            ( min === null && max === null ) ||
            ( min === null && date <= max ) ||
            ( min <= date   && max === null ) ||
            ( min <= date   && date <= max )
        ) {
            return true;
        }
        return false;
    }
);

var tblClient;
// START CALL DATATABLE
function getData(){

    tblClient = $('#list_data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "order": [[ 4, "desc" ]],
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id_goog_repo"},
            {"data": "nick"},
            {"data": "urls_gore"},
            {"data": "id_clai_gore",
                "render": function(data, type, row) {
                    return '<a href="#" style="text-decoration: none; color: inherit">'+ data +'</a>';
                }},
            {"data": "date_gore",
                "render": function(data, type, row) {
                    return '<a href="#" style="text-decoration: none; color: inherit">'+ data +'</a>';
                }},
            {"data": "type_clai_gore",
                "render": function(data, type, row) {
                    return '<a href="#" style="text-decoration: none; color: inherit">'+ data +'</a>';
                }},
            {"data": "type_clai_gore"},
        ],
        columnDefs: [
            {
                "targets": [ 0, 1, 2],
                "visible": false,
                "searchable": false
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" style="text-decoration: none; color: inherit"><label class="badge badge-success">Approved</label></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
}


// when document get ready
$(function () {
// Create date inputs
    minDate = new DateTime($('#min'), {
        format: 'YYYY-MM-DD'
    });
    maxDate = new DateTime($('#max'), {
        format: 'YYYY-MM-DD'
    });

    // call datatable
    getData();

    // Refilter the table
    $('#min, #max').on('change', function () {
        tblClient.draw();
    });


    $('#list_data tbody')
        .on('click', 'tr', 'a', function (){
            var data = tblClient.row( this ).data();

            document.getElementById("total_urls").innerHTML = data.cant_urls_gore;
            document.getElementById("id_claim").innerHTML = data.id_clai_gore;
            document.getElementById("type_content").innerHTML = data.type_clai_gore;
            document.getElementById("date_claim").innerHTML = data.date_gore;
            document.getElementById("urls_claim").innerHTML = data.urls_gore;
            $('#myModalClient').modal('show');
        });

});






