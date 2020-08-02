"""
Program: Ticket.py
Author: Paul Ford
Last date modified: 07/27/2020
Purpose: Ticket Class
"""
from datetime import datetime


class Ticket:
    """Tickets that will enter the queue and be displayed on the GUI"""

    def __init__(self, name, description, store_id, priority, status, time):
        """
        :param name: Name of the ticket the user submits
        :param description: a short description of the problem
        :param store_id: store ID will be a list of store to submit
        :param priority: The urgency of the ticket
        :param status: The status of the ticket in the queue
                       in progress, to do, complete, etc
        :param time: The time the ticket was submitted.
        """

        self._number = 0
        self._name = name
        self._description = description
        self._store_id = store_id
        self._priority = priority
        self._status = status
        self._date = time

    def __str__(self):
        """
        Displays for testing the tickets attributes.
        :return: un-formatted string
        """
        return str("Number: {}, Name: {}, Description: {}, storeID: {}, priority: {}, status: {}, Date: {} "
                   .format(self._number, self._name,
                           self._description, self._store_id, self._priority, self._status, self._date))

    def __repr__(self):
        """
        Nice Format for ticket
        :return: formatted string
        """
        return str("Ticket Number: {}\n"
                   "Ticket Name: {}\n"
                   "Description: {}\n"
                   "Store ID: {}\n"
                   "Priority: {}\n"
                   "Status: {}\n"
                   "Date Ticket was placed: {}\n"
                   "----------------------\n"
                   .format(self._number, self._name, self._description,
                           self._store_id, self._priority, self._status, self._date))

# driver
# date = datetime.now()
# Ticket1 = Ticket("this is bad", "description is short", "1234", "Emergency", "In queue", date)
# print(Ticket1)
# print(Ticket1.__repr__())
# print(Ticket1.__repr__())
