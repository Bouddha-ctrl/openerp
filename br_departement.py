from openerp.osv import osv,fields
import openerp

class br_departement(osv.osv):
    _name = 'br.departement'
    _columns={
        'name':fields.char('Nom'),
        'code'   :fields.char('Code'),
        
        'manager':fields.char('Manager'),
        'tel':fields.char('Tel'),
        'email':fields.char('Email')
        
    }
br_departement()