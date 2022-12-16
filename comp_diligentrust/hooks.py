from . import __version__ as app_version

app_name = "comp_diligentrust"
app_title = "Company Diligentrust"
app_publisher = "Muhammad Zubair form Diligentrust"
app_description = "Contain Blue Theme For Company DiligenTrust"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "zubairmazhar23@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/comp_diligentrust/css/diligen_app.css"
# app_include_js = "/assets/comp_diligentrust/js/comp_diligentrust.js"

# include js, css files in header of web template
web_include_css = "/assets/comp_diligentrust/css/diligen_web.css"
# web_include_js = "/assets/comp_diligentrust/js/comp_diligentrust.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "comp_diligentrust/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# before_install = "comp_diligentrust.install.before_install"
# after_install = "comp_diligentrust.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "comp_diligentrust.uninstall.before_uninstall"
# after_uninstall = "comp_diligentrust.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "comp_diligentrust.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "custom_app.overrides.CustomToDo"
	"PaymentRequest": "comp_diligentrust.overrides.Pay"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"comp_diligentrust.tasks.all"
#	],
#	"daily": [
#		"comp_diligentrust.tasks.daily"
#	],
#	"hourly": [
#		"comp_diligentrust.tasks.hourly"
#	],
#	"weekly": [
#		"comp_diligentrust.tasks.weekly"
#	]
#	"monthly": [
#		"comp_diligentrust.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "comp_diligentrust.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "comp_diligentrust.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "comp_diligentrust.task.get_dashboard_data"
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
#	"comp_diligentrust.auth.validate"
# ]

