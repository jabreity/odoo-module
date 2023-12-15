# -*- coding: utf-8 -*-
# from odoo import http


# class Fooby(http.Controller):
#     @http.route('/fooby/fooby', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fooby/fooby/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fooby.listing', {
#             'root': '/fooby/fooby',
#             'objects': http.request.env['fooby.fooby'].search([]),
#         })

#     @http.route('/fooby/fooby/objects/<model("fooby.fooby"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fooby.object', {
#             'object': obj
#         })

