from openerp.osv import osv,fields
import openerp

class br_courrier_interne(osv.osv):
    _name = 'br.courrier_interne'
    _columns={
        'code'   :fields.char('Code'),
        'date':fields.date('Date'),


        'expediteur':fields.many2one('br.departement','Expediteur',ondelete="cascade"),
        'destinataire':fields.many2one('br.departement','Destinataire',ondelete="cascade"),

        'adresse':fields.char('Adresse'),
        'objet':fields.char('Objet'),
        'pj':fields.binary('PJ',filters="*.pdf"),
        'contenu':fields.char('Contenu'),
        'transmission':fields.char('Contenu')
        
    }
br_courrier_interne()