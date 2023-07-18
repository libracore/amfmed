frappe.listview_settings['Asset'] = {
    'onload': function(listview) {
        listview.page.add_menu_item( __("Create depreciation entries in advance"), function() {
            create_depreciation_entries_in_advance();
        });
    }
}

function create_depreciation_entries_in_advance() {
    frappe.prompt(
        [
            {'fieldname': 'date', 'fieldtype': 'Date', 'label': __("Create depreciation entries until"), 'reqd': 1}  
        ],
        function(values){
            frappe.call({
                'method': 'amfmed.amf_medical.utils.create_depreciation_entries_in_advance',
                'args': {
                    'date': values.date
                },
                'callback': function(response) {
                    frappe.show_alert(response.message);
                }
            });
        },
        __('Create depreciation entries in advance'),
        __('Create')
    );
}

