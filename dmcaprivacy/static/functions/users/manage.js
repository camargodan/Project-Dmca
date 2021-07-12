var tblClient;
// START CALL DATATABLE
function getData(){
    tblClient = $('#list_data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "order": [[ 0, "desc" ]],
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "date_joined"},
            {
                "data": "imag_clie",
                "render": function(data, type, row) {
                    if (data){
                        return '<img src="'+data+'" />';
                    }
                }
            },
            {"data": "last_name",
                render: function(data, type, row, meta)
                 {
                     return row.first_name+' '+row.last_name;
                 },},
            {"data": "email"},
            {"data": "is_active",
                "render": function(data, type, row) {
                    if (data){
                        return '<input type="radio" class="form-check-input" checked="" value="True">';
                    }
                    else{
                        return '<input type="radio" class="form-check-input" disabled="" value="False">'
                    }
                }},
            {"data": "is_superuser",
                "render": function(data, type, row) {
                    if (data){
                        return '<input type="radio" class="form-check-input" checked="" value="True">';
                    }
                    else{
                        return '<input type="radio" class="form-check-input" disabled="" value="False">'
                    }
                }},
            {"data": "is_worker",
                "render": function(data, type, row) {
                    if (data){
                        return '<input type="radio" class="form-check-input" checked="" value="True">';
                    }
                    else{
                        return '<input type="radio" class="form-check-input" disabled="" value="False">'
                    }
                }},
            {"data": "is_client",
                "render": function(data, type, row) {
                    if (data){
                        return '<input type="radio" class="form-check-input" checked="" value="True">';
                    }
                    else{
                        return '<input type="radio" class="form-check-input" disabled="" value="False">'
                    }
                }},
            {"data": "email"},
        ],
        columnDefs: [
            {
                "targets": [ 0 ],
                "visible": false,
                "searchable": false
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit"><i class="fas fa-edit fa-lg"></i></a> ';
                    buttons += '<a href="#" rel="assign" style="margin-left: 10%"><i class="ti-split-h fa-lg"></i></a> ';
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
    //call datatable
    getData();

    $('#list_data tbody')
        .on('click', 'a[rel="assign"]', function (){
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            console.log(data);
            $('input[name="action"]').val('assign');
            $('input[name="id"]').val(data.id);
            $('select[name="plan_id"]').val(data.plan_id);
            $('select[name="id_worker"]').val(data.id_worker);
            $('#myModalClient2').modal('show');


        })
        .on('click', 'a[rel="edit"]', function (){
            modal_title.find('span').html('Edit selected user');
            modal_title.find('i').removeClass().addClass('ti-cut');
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();

            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="is_active"]').val(data.is_active).each(function() {
                if ($(this).val() == 'true') {
                    $(this).val('True');
                    $(this).prop('checked', true);
                } else{
                    $(this).val('False');
                    $(this).prop('checked', false);
                }
            });
            $('input[name="is_superuser"]').val(data.is_superuser).each(function() {
                if ($(this).val() == 'true') {
                    $(this).val('True');
                    $(this).prop('checked', true);
                } else{
                    $(this).val('False');
                    $(this).prop('checked', false);
                }
            });
            $('input[name="is_worker"]').val(data.is_worker).each(function() {
                if ($(this).val() == 'true') {
                    $(this).val('True');
                    $(this).prop('checked', true);
                } else{
                    $(this).val('False');
                    $(this).prop('checked', false);
                }
            });
            $('input[name="is_client"]').val(data.is_client).each(function() {
                if ($(this).val() == 'true') {
                    $(this).val('True');
                    $(this).prop('checked', true);
                } else{
                    $(this).val('False');
                    $(this).prop('checked', false);
                }
            });
            // modal call
            $('#myModalClient').modal('show');
        });

    // checkbox events
    $('input[name="is_active"]').click(function() {
        if ($(this).val() == 'True'){$(this).val('False');}
        else{$(this).val('True');}});
    $('input[name="is_superuser"]').click(function() {
        if ($(this).val() == 'True'){$(this).val('False');}
        else{$(this).val('True');}});
    $('input[name="is_worker"]').click(function() {
        if ($(this).val() == 'True'){$(this).val('False');}
        else{$(this).val('True');}});
    $('input[name="is_client"]').click(function() {
        if ($(this).val() == 'True'){$(this).val('False');}
        else{$(this).val('True');}});

    // open modal
    $('#myModalClient').on('shown.bs.modal', function () {
        // for the model reset all values in it.
        // $('form')[0].reset();
    });
    $('#myModalClient2').on('shown.bs.modal', function () {
        // for the model reset all values in it.
        // $('form')[0].reset();
    });
    // submit form
    $('form').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to save this User?', parameters, function () {
            $('#myModalClient').modal('hide');
            $('#myModalClient2').modal('hide');
            tblClient.ajax.reload();
        });
    });
});