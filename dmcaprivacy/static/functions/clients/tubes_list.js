var tblClient;
// START CALL DATATABLE
function getData(){
    tblClient = $('#list_data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "order": [[ 3, "desc" ]],
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id_tube_repo"},
            {"data": "tube_urls"},
            {"data": "date_tube",
                "render": function(data, type, row) {
                    return '<a href="#" style="text-decoration: none; color: inherit">'+ data +'</a>';
                },},
            {"data": "name_tube_page",
                "render": function(data, type, row) {
                    return '<a href="#" style="text-decoration: none; color: inherit">'+ data +'</a>';
                },},
            {"data": "cant_urls",
                "render": function(data, type, row) {
                    return '<a href="#" style="text-decoration: none; color: inherit">'+ data +'</a>';
                },},
            {"data": "name_tube_page"},
        ],
        columnDefs: [
            {
                "targets": [ 0, 1,],
                "visible": false,
                "searchable": false
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" style="text-decoration: none; color: inherit"><label class="badge badge-success">Approved</label></a> ';
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
    // call datatable
    getData();
    // call modal
    $('#list_data tbody')
        .on('click', 'tr', 'a', function (){
            var data = tblClient.row( this ).data();
            document.getElementById("num_url").innerHTML = data.cant_urls;
            document.getElementById("tube_name").innerHTML = data.name_tube_page;
            document.getElementById("date_tub").innerHTML = data.date_tube;
            document.getElementById("url_tubes").innerHTML = data.tube_urls;
            $('#myModalClient').modal('show');
        });
});