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


function getData2(){
    tblClient = $('#list_data2').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata2'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "nick"},
            {"data": "name_page"},
            {"data": "prio"},
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

    // button edit
    $('#list_data tbody')
        .on('click', 'a[rel="edit"]', function (){
            modal_title.find('span').html('Edit selected plan');
            modal_title.find('i').removeClass().addClass('ti-cut');
            var tr = tblClient.cell($(this).closest('td, li')).index();
            var data = tblClient.row(tr.row).data();
            getData2();

            $('#myModalClient').modal('show');
        })

});