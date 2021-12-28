from openerp.osv import osv,fields
import openerp

class br_courrier_arrive(osv.osv):

    def _draft_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'draft'})
        return True 
    
    def _waiting_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'waiting'})
        return True 

    def _approuved_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'approuved'})
        return True 
        
    def _delivered_fcn(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'delivered'})
        return True 



    _name = 'br.courrier_arrive'
    _columns={
        'code'   :fields.char('Code'),
        'date':fields.date('Date'),

        'expediteur':fields.many2one('br.organisation','Expediteur',ondelete="cascade"),
        'destinataire':fields.many2one('br.departement','Destinataire',ondelete="cascade"),


        'adresse':fields.char('Adresse'),
        'objet':fields.char('Objet'),
        'pj':fields.binary('PJ',filters="*.pdf"),
        'contenu':fields.text('Contenu'),

        'transmission':fields.selection([
                                        ('email','Email'),
                                        ('courier','Courier Postal'),
                                        ('faxe',"Faxe")
                                        ],'Canal de transmission'),

        'state':fields.selection([
                                    ('draft','Nouveau'),
                                    ('waiting','Waiting'),
                                    ('approuved','Approuved'),
                                    ('delivered','Delivered'),
                                    ],'State',readonly=True)

    }
br_courrier_arrive()