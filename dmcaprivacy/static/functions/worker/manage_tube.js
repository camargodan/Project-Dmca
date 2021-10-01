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
            {"data": "nick"},
            {"data": "date_tube"},
            {"data": "name_tube_page"},
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
            $('input[name="id_tube_repo"]').val(data.id_tube_repo);
            $('textarea[name="tube_urls"]').val(data.tube_urls);
            $('input[name="nick"]').val(data.nick);
            $('input[name="date_tube"]').val(data.date_tube);
            $('input[name="tube"]').val(data.name_tube_page);
            $('#myModalClient').modal('show');
        })
        .on('click', 'a[rel="delete"]', function (){
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id_tube_repo', data.id_tube_repo);
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