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
        self._ticket_number = 0
        self._ticketsDict = {}

    def addTicket(self, ticket):
        self._ticket_number += 1
        ticket._number = self._ticket_number
        self._ticketsDict[self._ticket_number] = ticket

    def removeTicket(self, key):
        self._ticketsDict.pop(key)

    def queueSize(self):
        return self._ticketsDict.__len__()

# Driver
# create tickets
date = datetime.now()
Ticket1 = Ticket("this is bad", "description is short", "1234", "Emergency", "In queue", date)
Ticket2 = Ticket("this is good", "description is short", "1234", "Emergency", "In queue", date)
tickets = TicketsQueue()
tickets.addTicket(Ticket1)
tickets.addTicket(Ticket2)
print(tickets._ticketsDict.__len__())
print(tickets._ticketsDict)
tickets.removeTicket(1)
print(tickets._ticketsDict)
print(len(tickets._ticketsDict))

