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
            {"data": "id_tube_pages"},
            {"data": "name_tube_page"},
            {"data": "name_tube_page"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" type="button" class="btn btn-warning py-1"><i class="ti-cut "></i></a> ';
                    buttons += '<a href="#" rel="delete" type="button" class="btn btn-danger py-1"><i class="ti-trash "></i></a>';
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
        modal_title.find('span').html('Add a new tube page');
        modal_title.find('i').removeClass().addClass('ti-plus');
        $('form')[0].reset();
        $('#myModalClient').modal('show');
    });
    // button edit
    $('#list_data tbody')
        .on('click', 'a[rel="edit"]', function (){
            modal_title.find('span').html('Edit selected tube page');
            modal_title.find('i').removeClass().addClass('ti-cut');
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id_tube_pages"]').val(data.id_tube_pages);
            $('input[name="name_tube_page"]').val(data.name_tube_page);
            $('#myModalClient').modal('show');

        })
        .on('click', 'a[rel="delete"]', function (){
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id_tube_pages', data.id_tube_pages);
            submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to delete this Tube page?', parameters, function () {
                tblClient.ajax.reload();
            });

        });
    // open modal
    $('#myModalClient').on('shown.bs.modal', function () {
        $('#name_tube_page').focus();
        // for the model reset all values in it.
        // $('form')[0].reset();
    });
    // submit form
    $('form').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to save this Tube Page?', parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
        });
    });

});