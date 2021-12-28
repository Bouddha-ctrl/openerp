from openerp.osv import osv,fields
import openerp

class br_courrier_externe(osv.osv):
    _name = 'br.courrier_externe'
    _columns={
        'code'   :fields.char('Code'),
        'date':fields.date('Date'),

        'expediteur':fields.many2one('br.departement','Expediteur',ondelete="cascade"),
        'destinataire':fields.many2one('br.organisation','Destinataire',ondelete="cascade"),


        'adresse':fields.char('Adresse'),
        'objet':fields.char('Objet'),
        'pj':fields.binary('PJ',filters="*.pdf"),
        'contenu':fields.char('Contenu'),
        'transmission':fields.char('Contenu')
        
    }
br_courrier_externe()