app_name = "farm_advisor"
app_title = "Farm Advisor"
app_publisher = "Bantoo"
app_description = "Farm management app built on frappe"
app_email = "devs@thebantoo.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/farm_advisor/css/farm_advisor.css"
# app_include_js = "/assets/farm_advisor/js/farm_advisor.js"

# include js, css files in header of web template
# web_include_css = "/assets/farm_advisor/css/farm_advisor.css"
# web_include_js = "/assets/farm_advisor/js/farm_advisor.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "farm_advisor/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "farm_advisor/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "farm_advisor.utils.jinja_methods",
# 	"filters": "farm_advisor.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "farm_advisor.install.before_install"
# after_install = "farm_advisor.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "farm_advisor.uninstall.before_uninstall"
# after_uninstall = "farm_advisor.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "farm_advisor.utils.before_app_install"
# after_app_install = "farm_advisor.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "farm_advisor.utils.before_app_uninstall"
# after_app_uninstall = "farm_advisor.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "farm_advisor.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"farm_advisor.tasks.all"
# 	],
# 	"daily": [
# 		"farm_advisor.tasks.daily"
# 	],
# 	"hourly": [
# 		"farm_advisor.tasks.hourly"
# 	],
# 	"weekly": [
# 		"farm_advisor.tasks.weekly"
# 	],
# 	"monthly": [
# 		"farm_advisor.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "farm_advisor.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "farm_advisor.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "farm_advisor.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["farm_advisor.utils.before_request"]
# after_request = ["farm_advisor.utils.after_request"]

# Job Events
# ----------
# before_job = ["farm_advisor.utils.before_job"]
# after_job = ["farm_advisor.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"farm_advisor.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
	{
		"dt": "Workflow State",
		"filters": [
			[
				"name", "in", [
					"Save Draft",
					"Draft",
					"Deposited",
					"Submitted for Deposit",
					"Deposit Accepted",
					"Deposit Rejected"
				]
			]
		]
	},
    {
		"dt": "Workflow",
		"filters": [
			[
				"name", "in", [
					"Farm Sale Deposit"
				]
			]
		]
	}
]

