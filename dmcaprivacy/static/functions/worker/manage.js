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
            {"data": "id_clie"},
            {"data": "plan"},
            {"data": "plan"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit"><i class="fas fa-edit fa-lg"></i></a> ';
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
});