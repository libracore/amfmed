# Copyright (c) 2023, libracore and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from erpnext.assets.doctype.asset.depreciation import make_depreciation_entry

@frappe.whitelist()
def create_depreciation_entries_in_advance(date):
    count = 0
    assets = frappe.get_all("Asset", filters={'status': 'Partially Depreciated'}, fields=['name']) 
    for asset in assets: 
        make_depreciation_entry(asset_name=asset['name'], date=date) 
        count += 1
        frappe.db.commit()
    
    return _("Created depreciation entries for {0} assets").format(count)
    
