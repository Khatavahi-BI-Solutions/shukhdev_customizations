from . import __version__ as app_version

app_name = "shukhdev_customizations"
app_title = "Shukhdev Customizations"
app_publisher = "Jigar Tarpara"
app_description = "Shukhdev Customizations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "jigartarpara@khatavahi.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shukhdev_customizations/css/shukhdev_customizations.css"
# app_include_js = "/assets/shukhdev_customizations/js/shukhdev_customizations.js"
app_include_js = "/assets/shukhdev_customizations/js/khatavahi.js"
# include js, css files in header of web template
# web_include_css = "/assets/shukhdev_customizations/css/shukhdev_customizations.css"
# web_include_js = "/assets/shukhdev_customizations/js/shukhdev_customizations.js"
app_include_css = "/assets/shukhdev_customizations/css/shukhdev.css"
# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "shukhdev_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Invoice" : "public/js/salesinvoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "shukhdev_customizations.install.before_install"
# after_install = "shukhdev_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "shukhdev_customizations.uninstall.before_uninstall"
# after_uninstall = "shukhdev_customizations.uninstall.after_uninstall"
after_migrate = "shukhdev_customizations.custom_field.setup_custom_fields"
# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shukhdev_customizations.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"validate": "shukhdev_customizations.sales_invoice.validate"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shukhdev_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"shukhdev_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"shukhdev_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shukhdev_customizations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"shukhdev_customizations.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "shukhdev_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shukhdev_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "shukhdev_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"shukhdev_customizations.auth.validate"
# ]

