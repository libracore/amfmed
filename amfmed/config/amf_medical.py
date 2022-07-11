from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Accounting"),
            "icon": "octicon octicon-git-compare",
            "items": [
                   {
                        "type": "page",
                        "name": "file_uploader",
                        "label": _("PINV uploader"),
                        "description": _("Bulk upload scanned purchase invoices")           
                   },                 
            ]
        },
        {
            "label": _("Switzerland"),
            "icon": "fa fa-money",
            "items": [
                    {
                       "type": "page",
                       "name": "bank_wizard",
                       "label": _("Bank Wizard"),
                       "description": _("Bank Wizard")
                    },
                    {
                       "type": "doctype",
                       "name": "Payment Proposal",
                       "label": _("Payment Proposal"),
                       "description": _("Payment Proposal")
                    },
                    {
                       "type": "doctype",
                       "name": "Payment Reminder",
                       "label": _("Payment Reminder"),
                       "description": _("Payment Reminder")
                    },
                    {
                       "type": "doctype",
                       "name": "VAT Declaration",
                       "label": _("VAT Declaration"),
                       "description": _("VAT Declaration")
                    },
                    {
                        "type": "report",
                        "name": "Kontrolle MwSt",
                        "label": _("Kontrolle MwSt"),
                        "doctype": "Sales Invoice",
                        "is_query_report": True
                    },
                    {
                       "type": "doctype",
                       "name": "Salary Certificate",
                       "label": _("Salary Certificate"),
                       "description": _("Salary Certificate")
                    },
                    {
                        "type": "report",
                        "name": "Worktime Overview",
                        "label": _("Worktime Overview"),
                        "doctype": "Timesheet",
                        "is_query_report": True
                    },
                    {
                       "type": "doctype",
                       "name": "ERPNextSwiss Settings",
                       "label": _("ERPNextSwiss Settings"),
                       "description": _("ERPNextSwiss Settings")                   
                    },
                    {
                       "type": "doctype",
                       "name": "Worktime Settings",
                       "label": _("Worktime Settings"),
                       "description": _("Worktime Settings")
                    },
                    {
                       "type": "doctype",
                       "name": "VAT query",
                       "label": _("VAT query"),
                       "description": _("VAT query")
                    }
            ]
        }
]
