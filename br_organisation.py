from openerp.osv import osv,fields
import openerp

class br_organisation(osv.osv):
    _name = 'br.organisation'
    _columns={
        'name':fields.char('Nom'),
        'code'   :fields.char('Code'),
        
        'adresse':fields.char('Adresse'),
        'tel':fields.char('Tel'),
        'email':fields.char('Email'),
        'siteweb':fields.char('Site Web')
    }
br_organisation()