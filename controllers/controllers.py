# -*- coding: utf-8 -*-
from odoo import http

# class CobaModule(http.Controller):
#     @http.route('/coba_module/coba_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coba_module/coba_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coba_module.listing', {
#             'root': '/coba_module/coba_module',
#             'objects': http.request.env['coba_module.coba_module'].search([]),
#         })

#     @http.route('/coba_module/coba_module/objects/<model("coba_module.coba_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coba_module.object', {
#             'object': obj
#         })