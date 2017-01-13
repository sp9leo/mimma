# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mimma"
app_title = "Mimma"
app_publisher = "mimma"
app_description = "mimma customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = " "
app_license = "MIT"
fixtures = ["Custom Field", "Custom Script", "Print Format", "Workflow"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mimma/css/mimma.css"
# app_include_js = "/assets/mimma/js/mimma.js"

# include js, css files in header of web template
# web_include_css = "/assets/mimma/css/mimma.css"
# web_include_js = "/assets/mimma/js/mimma.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mimma.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mimma.install.before_install"
# after_install = "mimma.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mimma.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mimma.tasks.all"
# 	],
# 	"daily": [
# 		"mimma.tasks.daily"
# 	],
# 	"hourly": [
# 		"mimma.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mimma.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mimma.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mimma.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mimma.event.get_events"
# }

