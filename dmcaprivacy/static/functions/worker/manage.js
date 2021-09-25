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
            {"data": "first_name",
                render: function(data, type, row, meta)
                {
                    return row.first_name+' '+row.last_name;
                },},
            {data: null,
                render: function(data, type, row, meta) {
                    var nick_pages = '';
                    //loop through all the row nick_pages to build output string
                    for (var item in row.nick_pages) {
                        var detail = row.nick_pages[item];
                        nick_pages = nick_pages + '✓ ' + detail.nick + ' - ' + detail.name_page + '</br>';
                    }
                    return nick_pages;

                }
            },
            {"data": "plan"},
            {"data": "plan"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="remove"><i class="far fa-eye-slash fa-lg"></i></a> ';
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

    //button to hide the entire row
    $('#list_data').on('click', '.remove', function () {
        var table = $('#list_data').DataTable();
        table
            .row($(this).parents('tr'))
            .remove()
            .draw();
    });

});