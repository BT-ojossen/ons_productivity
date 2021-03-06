# -*- coding: utf-8 -*-
#
#  File: __openerp__.py
#  Module: ons_productivity_accounting
#
#  dco@open-net.ch & cyp@open-net.ch & lfr@open-net.ch
#
#  Copyright (c) 2016-TODAY Open-Net Ltd. All rights reserved.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name' : 'Open Net Productivity: Accounting',
    'version' : '2.1',
    'author' : 'Open Net Sàrl',
    'category' : 'Accounting',
    'website': 'http://www.open-net.ch',
    'images' : [],
    'depends' : [
        'account',
        'l10n_ch'
    ],
    'data': [
        'views/onsp_accounting.xml',
        'views/view_invoices.xml',
        'views/view_partner_bank.xml',
        'views/view_account_move.xml'
    ],
    'js': [
    ],
    'qweb' : [
    ],
    'css':[
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
