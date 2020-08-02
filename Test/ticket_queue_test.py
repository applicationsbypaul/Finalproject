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

    def test_remove_ticket(self):
        """
        Now we remove the ticket and the size should return to 0
        and is empty should return to True
        """
        # add ticket first to be removed.
        self.queue.addTicket(self.ticket1)
        self.queue.removeTicket()
        self.assertEqual(self.queue.queueSize(), 0)
        self.assertEqual(self.queue._isEmpty, True)

    def test_next_ticket(self):
        """
        To test this we will add 3 tickets.
        First we test to see if next ticket returns ticket2 (Name: TicketName2)
        Then we will test after next ticket two more times it should move back to 1
        We will also test the current ticket, that indext should move along the ticket -1
        ie. if current ticket is 1 then ticket name will be 2
        """
        self.queue.addTicket(self.ticket1)
        self.queue.addTicket(self.ticket2)
        self.queue.addTicket(self.ticket3)
        # Since the queue starts at _current_ticket = 0
        # that means we call next and it should = 1 and the ticket name should be ticketname2
        self.queue.nextTicket()
        # first check if the ticket is the samethen
        self.assertEqual(self.queue.currentTicket(), self.ticket2)
        self.assertEqual(self.queue._current_ticket, 2)


if __name__ == '__main__':
    unittest.main()
