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
                {
                    "data": "imag_clie",
                    "render": function(data, type, row) {
                        if (data){
                            return '<img src="'+data+'" />';
                        }
                    }

                },
                {"data": "first_name"},
                {"data": "last_name"},
                {"data": "email"},
                {"data": "email"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/erp/category/update/' + row.id + '/" type="button" class="btn btn-warning py-1"><i class="ti-cut "></i></a> ';
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
        //call datatable
        getData();
    });