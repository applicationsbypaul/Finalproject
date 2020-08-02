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
        We will also test the current ticket, that index should move along the ticket -1
        ie. if current ticket is 1 then ticket name will be 2
        """
        self.helper_add_tickets()
        # Since the queue starts at _current_ticket = 0
        # that means we call next and it should = 1 and the ticket name should be ticket name2
        self.queue.nextTicket()
        self.assertEqual(self.queue.currentTicket(), self.ticket2)
        self.assertEqual(self.queue._current_ticket, 1)
        # now move next position twice to confirm its back at the begging. ._current ticket = 0
        # ticket should = Ticket 1
        self.queue.nextTicket()
        self.queue.nextTicket()
        self.assertEqual(self.queue.currentTicket(), self.ticket1)
        self.assertEqual(self.queue._current_ticket, 0)

    def test_prev_ticket(self):
        """
        To test this we will add 3 tickets.
        First we test to see if prev ticket returns ticket3 (Name: TicketName3)
        Then we will test after prev ticket two more times it should move back to ticketname1
        We will also test the current ticket, that index should move along the ticket -1
        ie. if current ticket is 1 then ticket name will be 2
        """
        self.helper_add_tickets()
        self.queue.previousTicket()
        self.assertEqual(self.queue.currentTicket(), self.ticket3)
        self.assertEqual(self.queue._current_ticket, 2)
        # move twice prev to confirm it moves
        self.queue.previousTicket()
        self.queue.previousTicket()
        self.assertEqual(self.queue.currentTicket(), self.ticket1)
        self.assertEqual(self.queue._current_ticket, 0)

    def test_empty_queue(self):
        """
        testing calling empty queue
        """
        # First add tickets
        self.helper_add_tickets()
        self.assertEqual(self.queue._isEmpty, False)
        self.queue.emptyQueue()
        self.assertEqual(self.queue.queueSize(), 0)
        self.assertEqual(self.queue._isEmpty, True)

    def test_priority_average(self):
        """
        This test is special since it lives in the ticket MainGui I wanted to test it
        I couldn't find a way to implement it so I decided to add a method that does the same thing
        """
        self.helper_add_tickets()
        print(self.average_priority())

    def helper_add_tickets(self):
        """
        Helper method to just add our test tickets.
        """
        self.queue.addTicket(self.ticket1)
        self.queue.addTicket(self.ticket2)
        self.queue.addTicket(self.ticket3)

    def average_priority(self):
        """
        This calculates the average priority level of the queue
        :return Rounded average of the current queue
        """
        priority_dic = {'Low': 1, 'Medium': 2, 'High': 3, 'Emergency': 4}
        total = 0
        for ticket in self.queue._ticket_list:
            if ticket._priority in priority_dic:
                total += priority_dic[ticket._priority]
        if total == 0:
            return 0
        return round(total / self.queue._ticket_list.__len__(), 2)


if __name__ == '__main__':
    unittest.main()
