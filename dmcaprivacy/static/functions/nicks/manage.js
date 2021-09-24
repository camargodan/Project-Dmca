var tblClient;
// START CALL DATATABLE
function getData(){
    tblClient = $('#list_data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id_nick"},
            {"data": "nick"},
            {"data": "name_page"},
            {"data": "prio"},
            {"data": "prio"},
        ],
        columnDefs: [
            {
                "targets": [0],
                "visible": false,
                "searchable": false
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit"><i class="fas fa-edit fa-lg"></i></a> ';
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
    // call datatable
    getData();

    // button edit
    $('#list_data tbody')
        .on('click', 'a[rel="edit"]', function (){
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            window.location.href = 'manage_nicks/edit/'+data.id_nick;
        })
        .on('click', 'a[rel="delete"]', function (){
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id_nick', data.id_nick);
            submit_with_ajax(window.location.pathname, 'Notification', "Are you sure to delete this Nick? Remember that you'll delete the nick in all the pages.", parameters, function () {
                tblClient.ajax.reload();
            });
        });

});