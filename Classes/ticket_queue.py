"""
Program: TicketQueue.py
Author: Paul Ford
Last date modified: 07/27/2020
Purpose: Class responsible for holding
the tickets in a queue
"""
from datetime import datetime

from Classes.ticket import Ticket


class TicketsQueue:
    def __init__(self):
        self._current_ticket = 0
        self._ticket_number = 0
        self._ticket_list = []
        self._isEmpty = False

    def addTicket(self, ticket):
        self._ticket_number += 1
        ticket._number = self._ticket_number
        ticket_index = (self._ticket_number, ticket)
        self._ticket_list.append(ticket_index)
        self._isEmpty = False

    def removeTicket(self):
        self._ticket_list.pop(self._current_ticket)
        self._current_ticket = 0
        if tickets.queueSize() == 0:
            self._isEmpty = True

    def queueSize(self):
        return self._ticket_list.__len__()

    def emptyQueue(self):
        self._ticket_list.clear()
        self._current_ticket = 0
        self._isEmpty = True

    def nextTicket(self):
        if self._current_ticket == self._ticket_list.__len__() - 1:
            self._current_ticket = 0
            print(self._ticket_list[self._current_ticket])
        else:
            print(self._ticket_list[self._current_ticket + 1])
            self._current_ticket += 1

    def currentTicket(self):
        print(self._ticket_list[self._current_ticket])

    def previousTicket(self):
        if self._current_ticket == 0:
            self._current_ticket = self._ticket_list.__len__() - 1
            print(self._ticket_list[self._current_ticket])
        else:
            print(self._ticket_list[self._current_ticket - 1])
            self._current_ticket -= 1


# Driver
# create tickets
date = datetime.now()
Ticket1 = Ticket("this is bad", "description is short", "1234", "Emergency", "In queue", date)
Ticket2 = Ticket("this is good", "description is short", "1234", "Emergency", "In queue", date)
Ticket3 = Ticket("this is great", "description is short", "1234", "Emergency", "In queue", date)
tickets = TicketsQueue()
tickets.addTicket(Ticket1)
tickets.addTicket(Ticket2)
tickets.addTicket(Ticket3)
tickets.nextTicket()
tickets.nextTicket()
tickets.nextTicket()
print(tickets.queueSize())
tickets.removeTicket()
print(tickets.queueSize())
tickets.currentTicket()
tickets.nextTicket()
tickets.nextTicket()
tickets.nextTicket()
tickets.nextTicket()
tickets.emptyQueue()
