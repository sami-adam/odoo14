# -*- coding: utf-8 -*-
# from odoo import http


# class Fit-hub(http.Controller):
#     @http.route('/fit-hub/fit-hub/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fit-hub/fit-hub/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fit-hub.listing', {
#             'root': '/fit-hub/fit-hub',
#             'objects': http.request.env['fit-hub.fit-hub'].search([]),
#         })

#     @http.route('/fit-hub/fit-hub/objects/<model("fit-hub.fit-hub"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fit-hub.object', {
#             'object': obj
#         })
