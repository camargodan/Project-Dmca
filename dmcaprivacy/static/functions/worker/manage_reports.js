var tblClient;
// START CALL DATATABLE
function getData(){
    tblClient = $('#list_data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "order": [[ 5, "desc" ]],
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
            {"data": "clients_id_clie_id"},
            {"data": "nick"},
            {"data": "urls_gore"},
            {"data": "id_clai_gore"},
            {"data": "date_gore"},
            {"data": "type_clai_gore"},
            {"data": "type_clai_gore"},
        ],
        columnDefs: [
            {
                "targets": [ 0, 1, 2, 3],
                "visible": false,
                "searchable": false
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" ><i class="fas fa-edit fa-lg"></i></a> ';
                    buttons += '<a href="#" rel="delete" style="margin-left: 10%"><i class="fas fa-trash-alt fa-lg"></i></a>';
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
        .on('click', 'a[rel="edit"]', function (){
            modal_title.find('span').html('Edit selected report');
            modal_title.find('i').removeClass().addClass('ti-cut');
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id_goog_repo"]').val(data.id_goog_repo);
            $('input[name="clients_id_clie_id"]').val(data.clients_id_clie_id);
            $('input[name="nick"]').val(data.nick);
            $('textarea[name="urls_gore"]').val(data.urls_gore);
            $('input[name="id_clai_gore"]').val(data.id_clai_gore);
            $('input[name="date_gore"]').val(data.date_gore);
            $('select[name="type_clai_gore"]').val(data.type_clai_gore);
            $('#myModalClient').modal('show');
        })
        .on('click', 'a[rel="delete"]', function (){
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id_goog_repo', data.id_goog_repo);
            submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to delete this Report?', parameters, function () {
                tblClient.ajax.reload();
            });
        });

    // submit form
    $('form').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to save this Report?', parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
        });
    });

});