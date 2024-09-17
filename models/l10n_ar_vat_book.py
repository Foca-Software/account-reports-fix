# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, models
from odoo.exceptions import UserError
from collections import OrderedDict
from odoo.tools.misc import format_date
import re
import json


class L10nARVatBook(models.AbstractModel):

    _inherit = "l10n_ar.vat.book"

    def _get_columns_name(self, options):
        res=super(L10nARVatBook, self)._get_columns_name(options)
        print('res:',res)
        indice=-1
        i=0
        for item in res:
            if item['name']=='CUIT':
                indice=i
            i+=1
        print('indice:',indice)
        if indice!=-1:
            res[indice]['name']="CUIT/DNI"
        print('res despues:',res)
        return res
