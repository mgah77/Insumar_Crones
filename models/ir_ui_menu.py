from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    def _load_menus_blacklist(self):
        blacklist = super()._load_menus_blacklist()

        _logger.warning("==== INICIO DEPURACIÓN ====")
        
        # 1. ¿Qué valor real tiene el campo?
        # Usamos getattr por seguridad
        tiene_reparos = getattr(self.env.company, 'has_reparos', False)
        _logger.warning("Valor de has_reparos: %s", tiene_reparos)
        _logger.warning("ID de la compañía: %s", self.env.company.id)

        # 2. ¿Encuentra el menú?
        try:
            menu = self.env.ref('tu_modulo.menu_reparos_root')
            _logger.warning("Menú encontrado ID: %s", menu.id)
            _logger.warning("Nombre del menú: %s", menu.name)
            
            # 3. ¿Lo mete en la lista?
            if not tiene_reparos:
                blacklist.append(menu.id)
                _logger.warning("ACCION: Añadido a blacklist. ID: %s", menu.id)
            else:
                _logger.warning("ACCION: No se añade a blacklist porque has_reparos es True")

        except Exception as e:
            _logger.warning("ERROR buscando menú: %s", e)

        _logger.warning("==== FIN DEPURACIÓN ====")

        return blacklist