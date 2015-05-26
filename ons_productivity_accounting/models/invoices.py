# -*- coding: utf-8 -*-
#
#  File: models/invoices.py
#  Module: ons_productivity_accounting
#
#  Created by cyp@open-net.ch
#
#  Copyright (c) 2013-TODAY Open Net Sàrl. All rights reserved.
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api

class account_invoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def unlink(self):
        for inv in self:
            if inv.state in ('draft', 'cancel'):
                self.write({'internal_number': False})
    
        return super(account_invoice, self).unlink()

