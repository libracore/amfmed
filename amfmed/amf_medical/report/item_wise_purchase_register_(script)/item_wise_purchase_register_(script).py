# Copyright (c) 2022, libracore and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Item"), "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 100},
        {"label": _("Item name"), "fieldname": "item_name", "fieldtype": "Data", "width": 150},
        {"label": _("Item Group"), "fieldname": "item_group", "fieldtype": "Link", "options": "Item Group", "width": 100},
        {"label": _("Description"), "fieldname": "description", "fieldtype": "Data", "width": 150},
        {"label": _("Invoice"), "fieldname": "invoice", "fieldtype": "Link", "options": "Purchase invoice", "width": 100},
        # {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": _("Date"), "fieldname": "posting_date", "fieldtype": "Date", "width": 80},
        {"label": _("Supplier"), "fieldname": "supplier", "fieldtype": "Link", "options": "Supplier", "width": 120},
        {"label": _("Supplier name"), "fieldname": "supplier_name", "fieldtype": "Data", "width": 120},
        {"label": _("Payable account"), "fieldname": "payable_account", "fieldtype": "Link", "options": "Account", "width": 80},
        {"label": _("Mode of Payment"), "fieldname": "mode_of_payment", "fieldtype": "Data", "width": 100},
        {"label": _("Project"), "fieldname": "project", "fieldtype": "Link", "options": "Project", "width": 100},
        {"label": _("Subproject"), "fieldname": "subproject", "fieldtype": "Link", "options": "Project", "width": 100},
        {"label": _("Purchase Order"), "fieldname": "purchase_order", "fieldtype": "Link", "options": "Purchase Order", "width": 100},
        {"label": _("Purchase Receipt"), "fieldname": "purchase_receipt", "fieldtype": "Link", "options": "Purchase Receipt", "width": 100},
        {"label": _("Expense account"), "fieldname": "expense_account", "fieldtype": "Link", "options": "Account", "width": 80},
        {"label": _("Stock Qty"), "fieldname": "stock_qty", "fieldtype": "Float", "precision": 2, "width": 80},
        {"label": _("Stock UOM"), "fieldname": "stock_uom", "fieldtype": "Link", "options": "UOM", "width": 80},
        {"label": _("Currency"), "fieldname": "currency", "fieldtype": "Link", "options": "Currency", "width": 80},
        {"label": _("Rate"), "fieldname": "rate", "fieldtype": "Float", "precision": 2, "width": 80},
        {"label": _("Amount"), "fieldname": "amount", "fieldtype": "Float", "precision": 2, "width": 80},
        {"label": "", "fieldname": "blank", "fieldtype": "Data", "width": 20}
    ]

def get_data(filters):
    if type(filters) is str:
        filters = ast.literal_eval(filters)
    else:
        filters = dict(filters)
   
    conditions = ""
    if 'supplier' in filters and filters['supplier']:
        conditions += """ AND `tabPurchase Invoice`.`supplier` = "{0}" """.format(filters['supplier'])
    if 'item' in filters and filters['item']:
        conditions += """ AND `tabPurchase Invoice Item`.`item_code` = "{0}" """.format(filters['item'])
    if 'project' in filters and filters['project']:
        conditions += """ AND `tabPurchase Invoice Item`.`project` = "{0}" """.format(filters['project'])
    if 'subproject' in filters and filters['subproject']:
        conditions += """ AND `tabPurchase Invoice`.`subproject` = "{0}" """.format(filters['subproject'])
        
    # prepare query
    sql_query = """
        SELECT 
            `tabPurchase Invoice Item`.`item_code` AS `item_code`,
            `tabPurchase Invoice Item`.`item_name` AS `item_name`,
            `tabItem`.`item_group` AS `item_group`,
            `tabPurchase Invoice Item`.`description` AS `description`,
            `tabPurchase Invoice Item`.`parent` AS `invoice`,
            `tabPurchase Invoice`.`status` AS `status`,
            `tabPurchase Invoice`.`posting_date` AS `posting_date`,
            `tabPurchase Invoice`.`supplier` AS `supplier`,
            `tabPurchase Invoice`.`supplier_name`AS `supplier_name`,
            `tabPurchase Invoice`.`credit_to` AS `payable_account`,
            `tabPayment Entry`.`mode_of_payment` AS `mode_of_payment`,
            `tabPurchase Invoice Item`.`project` AS `project`,
            `tabPurchase Invoice Item`.`subproject` AS `subproject`,
            `tabPurchase Invoice Item`.`purchase_order` AS `purchase_order`,
            `tabPurchase Invoice Item`.`purchase_receipt` AS `purchase_receipt`,
            `tabPurchase Invoice Item`.`expense_account` AS `expense_account`,
            `tabPurchase Invoice Item`.`stock_qty` AS `stock_qty`,
            `tabPurchase Invoice Item`.`stock_uom` AS `stock_uom`,
            `tabPurchase Invoice`.`currency` AS `currency`,
            `tabPurchase Invoice Item`.`rate` AS `rate`,
            `tabPurchase Invoice Item`.`amount` AS `amount`
        FROM `tabPurchase Invoice Item`
        LEFT JOIN `tabPurchase Invoice` ON `tabPurchase Invoice`.`name` = `tabPurchase Invoice Item`.`parent`
        LEFT JOIN `tabItem` ON `tabItem`.`name` = `tabPurchase Invoice Item`.`item_code`
        LEFT JOIN `tabPayment Entry Reference` ON `tabPayment Entry Reference`.`reference_name` = `tabPurchase Invoice`.`name`
        LEFT JOIN `tabPayment Entry` ON `tabPayment Entry`.`name` = `tabPayment Entry Reference`.`parent`
        WHERE 
            `tabPurchase Invoice`.`docstatus` = 1
            AND `tabPurchase Invoice`.`posting_date` >= "{from_date}"
            AND `tabPurchase Invoice`.`posting_date` <= "{to_date}"
            {conditions}
      ;
      """.format(
        from_date=filters['from_date'], 
        to_date=filters['to_date'],
        conditions=conditions
    )
    
    data = frappe.db.sql(sql_query, as_dict=1)

    return data
