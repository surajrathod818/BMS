# Copyright (c) 2024, Suraj Rathod and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BMSItem(Document):
	def validate(self):
		print("***************",self.name)

	def on_submit(self):
		doc = frappe.new_doc('Item')
		doc.item_code = self.item_name
		doc.item_group = "Consumable"
		doc.stock_uom = self.uom
		doc.insert()
    
	def on_cancel(self):
		doc = frappe.get_doc('Item',self.item_name)
		doc.disabled = True
		doc.save()

		

