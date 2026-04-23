from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    def _blacklist(self):
        
        tiene_reparos = getattr(self.env.company, 'has_reparos', False)

        try:
            menu = self.env.ref('Insumar_Crones.menu_customer_invoices_reparo')
            menu_id = menu.id
            if not tiene_reparos:
                menu.active = False   
            else:
                menu.active = True

        except Exception as e:
            _logger.warning("ERROR", e)

        return