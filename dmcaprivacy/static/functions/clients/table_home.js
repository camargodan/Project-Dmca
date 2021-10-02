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
    var modal_title = $('.modal-title');
    // call datatable
    getData();

    $('#list_data tbody')
        .on('click', 'tr', 'a', function (){
            var data = tblClient.row( this ).data();

            document.getElementById("total_urls").innerHTML = data.cant_urls_gore;
            document.getElementById("id_claim").innerHTML = data.id_clai_gore;
            document.getElementById("type_content").innerHTML = data.type_clai_gore;
            document.getElementById("date_claim").innerHTML = data.date_gore;
            document.getElementById("urls_claim").innerHTML = data.urls_gore;


            // var tr = tblClient.cell($(this).closest('td, li')).index();
            // var data = tblClient.row(tr.row).data();
            // $('input[name="action"]').val('edit');
            // $('input[name="id_goog_repo"]').val(data.id_goog_repo);
            // $('input[name="nick"]').val(data.nick);
            // $('textarea[name="urls_gore"]').val(data.urls_gore);
            // $('input[name="id_clai_gore"]').val(data.id_clai_gore);
            // $('input[name="date_gore"]').val(data.date_gore);
            // $('select[name="type_clai_gore"]').val(data.type_clai_gore);
            $('#myModalClient').modal('show');
        });


});