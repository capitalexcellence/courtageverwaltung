# Copyright (c) 2025, Capital Excellence GmbH and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestCourtageabrechnung(UnitTestCase):
	"""
	Unit tests for Courtageabrechnung.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestCourtageabrechnung(IntegrationTestCase):
	"""
	Integration tests for Courtageabrechnung.
	Use this class for testing interactions between multiple components.
	"""

	pass
