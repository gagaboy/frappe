# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe

def get_context(context):
	return { "doc": frappe.get_doc("About Us Settings", "About Us Settings") }
