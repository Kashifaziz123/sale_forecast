# -*- coding: utf-8 -*-
from odoo import http

# class SaleForecast(http.Controller):
#     @http.route('/sale_forecast/sale_forecast/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_forecast/sale_forecast/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_forecast.listing', {
#             'root': '/sale_forecast/sale_forecast',
#             'objects': http.request.env['sale_forecast.sale_forecast'].search([]),
#         })

#     @http.route('/sale_forecast/sale_forecast/objects/<model("sale_forecast.sale_forecast"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_forecast.object', {
#             'object': obj
#         })