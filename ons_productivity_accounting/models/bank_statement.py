# -*- coding: utf-8 -*-
# © 2016 Coninckx David (Open Net Sarl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields

class bank_statement(models.Model):
    _inherit = 'account.bank.statement'

    payment_order_lines = fields.Many2many('account.payment.line', string="Payment lines")