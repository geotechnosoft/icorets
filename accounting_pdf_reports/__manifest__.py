# -*- coding: utf-8 -*-

{
    'name': 'Odoo 16 Accounting Financial Reports',
    'version': '16.0.2.0.4',
    'category': 'Invoicing Management',
    'description': 'Accounting Reports For Odoo 16, Accounting Financial Reports, '
                   'Odoo 16 Financial Reports',
    'summary': 'Accounting Reports For Odoo 16',
    'sequence': '1',
    'author': 'Odoo Mates, Odoo SA',
    'license': 'LGPL-3',
    'company': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'support': 'odoomates@gmail.com',
    'website': 'https://www.youtube.com/watch?v=yA4NLwOLZms',
    'depends': ['account'],
    'live_test_url': 'https://www.youtube.com/watch?v=yA4NLwOLZms',
    'data': [
        'security/ir.model.access.csv',
        # 'data/account_account_type.xml',
        # 'views/menu.xml',
        # 'views/ledger_menu.xml',
        # 'views/financial_report.xml',
        'views/res_partner_view.xml',
        'views/settings.xml',
        'wizard/account_report_common_view.xml',
        'wizard/partner_ledger.xml',
        # 'wizard/general_ledger.xml',
        # 'wizard/trial_balance.xml',
        # 'wizard/balance_sheet.xml',
        # 'wizard/profit_and_loss.xml',
        # 'wizard/tax_report.xml',
        # 'wizard/aged_partner.xml',
        # 'wizard/journal_audit.xml',
        # 'wizard/vendor_balance_confirmation.xml',
        'report/report.xml',
        'report/report_partner_ledger.xml',
        # 'report/report_general_ledger.xml',
        # 'report/report_trial_balance.xml',
        # 'report/report_financial.xml',
        # 'report/report_tax.xml',
        # 'report/report_aged_partner.xml',
        # 'report/report_journal_audit.xml',
        # 'report/report_journal_entries.xml',

    ],
    'pre_init_hook': '_pre_init_clean_m2m_models',
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
}
