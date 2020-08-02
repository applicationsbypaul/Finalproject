import datetime
import unittest

from Classes.ticket import Ticket

# Date for the ticket
date = datetime.datetime.now().replace(microsecond=0)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # normal ticket
        self.ticket = Ticket('TicketName', 'TicketDescription', '1235', 'Emergency', 'In Queue', date)

    def tearDown(self):
        del self.ticket

    def test_ticket_raise_value_error(self):
        """
        creates a bad ticket and checks that the value raised error happens
        """
        with self.assertRaises(ValueError):
            ticket = Ticket('TicketName', 'TicketDescription', 'word', 'Emergency', 'In Queue', date)

    def test_valid_storeID(self):
        """
        Testing to confirm that the storeID when all numbers is valid
        """
        self.assertEqual(self.ticket._store_id, '1235')

    def test_que_creation(self):
        pass




if __name__ == '__main__':
    unittest.main()
