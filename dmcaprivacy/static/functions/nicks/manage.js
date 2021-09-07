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
            {"data": "prio"},
            {"data": "name_page"},
            {"data": "prio"},
        ],
        columnDefs: [
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
    var modal_title = $('.modal-title');
    // call datatable
    getData();
    // button add new
    $('#btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Add a new page');
        modal_title.find('i').removeClass().addClass('ti-plus');
        $('form')[0].reset();
        $('#myModalClient').modal('show');
    });
    // button edit
    $('#list_data tbody')
        .on('click', 'a[rel="edit"]', function (){
            modal_title.find('span').html('Edit selected page');
            modal_title.find('i').removeClass().addClass('ti-cut');
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id_page"]').val(data.id_page);
            $('input[name="name_page"]').val(data.name_page);
            $('#myModalClient').modal('show');

        })
        .on('click', 'a[rel="delete"]', function (){
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id_page', data.id_page);
            submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to delete this page?', parameters, function () {
                tblClient.ajax.reload();
            });

        });
    // open modal
    $('#myModalClient').on('shown.bs.modal', function () {
        $('#name_page').focus();
        // for the model reset all values in it.
        // $('form')[0].reset();
    });
    // submit form
    $('form').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to save this Page?', parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
        });
    });

});