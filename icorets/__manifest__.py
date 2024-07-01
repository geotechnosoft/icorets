{
    'name': 'Icore',
    'version': '1.2',
    'summary': 'ACcessories and product',
    'sequence': -100,
    'description': """ product """,
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends': ['base', 'sale', 'product','sale_stock','stock','account', 'approvals', 'account_accountant','purchase','l10n_in','l10n_in_hr_payroll','po_accounting_v16', 'hr_contract'],
    'license': 'LGPL-3',
    'application': True,
    'data': ['security/ir.model.access.csv',
             'views/icore_field.xml',
             'data/forecast_sequence.xml',
             'views/inherit_res_partner_view.xml',
             'views/inherit_stock_warehouse_view.xml',
             'views/forecast_order_view.xml',
             'views/inherit_approval_request_view.xml',
             'views/location_report_view.xml',
             'views/hr_contract_view.xml',
             'wizard/forecast_order_wiz_view.xml',
             'wizard/stock_variant_report_excel_view.xml',
             'wizard/short_close.xml',
             'report/credit_note.xml',
             'report/debit_note.xml',
             'report/amazon.xml',
             'report/flipkart_report.xml',
             'report/myntra_report.xml',
             'report/creditnote_urban.xml',
             'report/tax_invoice.xml',
             'report/purchase_order_report.xml',
             'report/book_my_show.xml',
             'report/fynd_mishop.xml',
             'report/retail_pro.xml',
             'report/proforma_inv.xml',
             'report/report_actions.xml',
             ],
    'website': 'https://planet-odoo.com/',
    'installable': True,
    'auto_install': False,

}
