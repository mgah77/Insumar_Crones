from odoo import models, api

class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    def _load_menus_blacklist(self):
        raise Exception("SI VES ESTO, EL CÓDIGO SE ESTÁ EJECUTANDO")
        blacklist = super()._load_menus_blacklist()

        if not self.env.company.has_reparos:
            menu = self.env.ref('Insumar_Crones.menu_customer_invoices_reparo')
            blacklist.append(menu.id)

        return blacklist