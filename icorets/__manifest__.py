{
    'name': 'Icore',
    'version': '1.2',
    'summary': 'ACcessories and product',
    'sequence': -100,
    'description': """ product """,
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends': ['base', 'sale', 'product','stock'],
    'license': 'LGPL-3',
    'application': True,
    'data': ['security/ir.model.access.csv',
             'views/icore_field.xml',
             'report/credit_note.xml',
             'report/debit_note.xml',
             'report/amazon.xml',
             'report/flipkart_report.xml',
             'report/myntra_report.xml',
             'report/urban_swing.xml',
             'report/creditnote_urban.xml',
             'report/tax_invoice.xml',
             'report/purchase_order_report.xml',
             ],
    'website': 'https://planet-odoo.com/',
    'installable': True,
    'auto_install': False,

}
