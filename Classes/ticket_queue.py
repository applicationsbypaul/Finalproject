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
        """
        index of current ticket thats being viewed
        the number associated with the ticket
        all the tickets

        """
        self._current_ticket = 0
        self._ticket_number = 0
        self._ticket_list = []
        self._isEmpty = False

    def addTicket(self, ticket):
        """
        Adds a ticket to the list of tickets
        :param ticket: Incoming ticket to be added
        :return:
        """
        # increase the ticket number that gets placed on the ticket
        self._ticket_number += 1
        # add the ticket number to the actually ticket
        ticket._number = self._ticket_number
        # create a tuple to represent the position and the ticket
        # add to list and set isEmpty to False
        self._ticket_list.append(ticket)
        self._isEmpty = False

    def removeTicket(self):
        """
        Removes the ticket from the list
        checks to see if the list is empty
        """
        self._ticket_list.pop(self._current_ticket)
        self._current_ticket = 0
        if self._ticket_list.__len__() == 0:
            self._isEmpty = True

    def queueSize(self):
        """
        :return: Size of the list
        """
        return self._ticket_list.__len__()

    def emptyQueue(self):
        """
        Empty the queue and set isEmpty to true
        """
        self._ticket_list.clear()
        self._current_ticket = 0
        self._isEmpty = True

    def nextTicket(self):
        """
        Sets the value of the current ticket to the next
        if its at the end of the list it sets it back at
        the start of the list
        """
        if self._current_ticket == self._ticket_list.__len__() - 1:
            self._current_ticket = 0
            return self._ticket_list[self._current_ticket]
        else:
            var = (self._ticket_list[self._current_ticket + 1])
            self._current_ticket += 1
            return var

    def currentTicket(self):
        """
        :return: The current ticket in the queue
        """
        return self._ticket_list[self._current_ticket]

    def previousTicket(self):
        """
        Sets the value of current ticket to the previous
        ticket in the queue. If it is at the beginning
        it will set the current ticket to the end of the list.
        :return:
        """
        if self._current_ticket == 0:
            self._current_ticket = self._ticket_list.__len__() - 1
            return self._ticket_list[self._current_ticket]
        else:
            var = (self._ticket_list[self._current_ticket - 1])
            self._current_ticket -= 1
            return var


# Driver
 #create tickets
#date = datetime.now()
#Ticket1 = Ticket("this is bad", "description is short", "1234", "Emergency", "In queue", date)
#Ticket2 = Ticket("this is good", "description is short", "1234", "Emergency", "In queue", date)
#Ticket3 = Ticket("this is great", "description is short", "1234", "Emergency", "In queue", date)
#tickets = TicketsQueue()
#tickets.addTicket(Ticket1)
#tickets.addTicket(Ticket2)
#tickets.addTicket(Ticket3)
#tickets.nextTicket()
#tickets.nextTicket()
#tickets.nextTicket()
#tickets.nextTicket()
#print(tickets.queueSize())
#tickets.removeTicket()
#print(tickets.queueSize())
#tickets.currentTicket()
#tickets.nextTicket()
#tickets.nextTicket()
#tickets.nextTicket()
#tickets.nextTicket()
#tickets.emptyQueue()
