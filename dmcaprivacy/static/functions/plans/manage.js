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
                {"data": "id_plan"},
                {"data": "plan"},
                {"data": "plan"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/erp/category/update/' + row.id + '/" type="button" class="btn btn-warning py-1"><i class="ti-cut "></i></a> ';
                        buttons += '<a href="/erp/category/delete/' + row.id + '/" type="button" class="btn btn-danger py-1"><i class="ti-trash "></i></a>';
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

        getData();
        // button add new
        $('#create-plan').on('click', function () {
            $('input[name="action"]').val('add');
            $('#myModalClient').modal('show');
        });
        // open modal
        $('#myModalClient').on('shown.bs.modal', function () {
            $('#plan').focus();
            $('form')[0].reset();
        });
        // submit form
        $('form').on('submit', function (e) {
            e.preventDefault();
            //var parameters = $(this).serializeArray();
            var parameters = new FormData(this);
            submit_with_ajax(window.location.pathname, 'Notification', 'Are you sure to do this action?', parameters, function () {
                $('#myModalClient').modal('hide');
                tblClient.ajax.reload();
            });
        });

    });