# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import randint

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Titulo", required=True, help="Nombre que tendrá el curso")
    description = fields.Text()
    course_icon = fields.Image(string="Icono", help="Icono para el curso")

    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="Responsible")
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

    codigo = fields.Char(compute='_compute_name')

    @api.depends('name')
    def _compute_name(self):
        for curso in self:
            curso.codigo = f"{curso.name}{randint(1, 1000)}"


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'
#     _description = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100