"""
Program: TicketQueue.py
Author: Paul Ford
Last date modified: 07/27/2020
Purpose: Class responsible for holding
the tickets in a queue
"""
from Classes.ticket import Ticket


class TicketQueue:

    def __int__(self):
        self._TicketNumber = 0
        self._tickets = {}

    def addTicket(self, key, ticket):
        key = self._TicketNumber + 1
        self._tickets[key] = ticket

    def removeTicket(self, key):
        self._tickets.pop(key)


# Driver
# create tikcets

Ticket1 = Ticket("this is bad", "description is short", "1234", "Emergency", "In queue", )
