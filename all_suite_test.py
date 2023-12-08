import unittest
from unittest.loader import makeSuite

from test_cases.test_add_player import TestAddPlayer
from test_cases.test_dashboard import TestDashboardPage
from test_cases.test_log_in_to_the_system import TestLoginPage
from test_cases.test_players_page import TestPlayersPage


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestDashboardPage))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestPlayersPage))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())