import unittest
from datetime import datetime

from Classes.ticket import Ticket
from Classes.ticket_queue import TicketsQueue

# Date for the ticket
date = datetime.now().replace(microsecond=0)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = TicketsQueue()
        self.ticket1 = Ticket('TicketName1', 'TicketDescription', '1235', 'Low', 'In Queue', date)
        self.ticket2 = Ticket('TicketName2', 'TicketDescription', '1235', 'Medium', 'In Queue', date)
        self.ticket3 = Ticket('TicketName3', 'TicketDescription', '1235', 'Emergency', 'In Queue', date)

    def tearDown(self):
        del self.queue
        del self.ticket1
        del self.ticket2
        del self.ticket3

    def test_queue_object_creation(self):
        """
        when the queue is initialized should be zero in the list
        and point current ticket should also be at zero 0
        """
        self.assertEqual(self.queue._current_ticket, 0)
        self.assertEqual(self.queue._isEmpty, True)

    def test_add_ticket(self):
        """
        When adding a ticket we should get the list length to 1
        and get isEmpty to False
        """
        self.queue.addTicket(self.ticket1)
        self.assertEqual(self.queue.queueSize(), 1)
        self.assertEqual(self.queue._isEmpty, False)


if __name__ == '__main__':
    unittest.main()