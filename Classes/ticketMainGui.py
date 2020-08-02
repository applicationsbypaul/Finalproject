import tkinter
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter.ttk import *
from Classes.ticket import Ticket
from Classes.ticket_database import *
from Classes.ticket_queue import TicketsQueue

# create the ticket queue to start the program
queue = TicketsQueue()
# a dictionary used later to evaluate the average of the tickets
priority = {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Emergency'}
# a lists of tuples used to display on the view tickets view
modes = [(1, "Low"), (2, "Medium"), (3, "High"), (4, "Emergency")]
conn = create_connection("ticketsdb.db")


# MAIN Menu View
class MainMenu:
    global queue

    def __init__(self, master):
        """
        :param master: current view
        """
        self.master = master
        self.master.title("Ticket Queue")
        # Lables and Buttons
        self.master.greetingLabel = tk.Label(self.master, text="Welcome to Ticket Creator")
        self.master.greetingLabel.pack()
        self.master.addTicketButton = tk.Button(self.master, text="Add New Ticket", bg="green", fg="white",
                                                command=self.gotoAddTicket)
        self.master.addTicketButton.pack()

        self.master.viewTicketButton = tk.Button(self.master, text="View Tickets", bg="blue", fg="white",
                                                 command=self.gotoViewTicket)
        self.master.viewTicketButton.pack()

    def gotoAddTicket(self):
        """
        Sets the top level to main menu
        Sets view size and starts to create the add view
        """
        add_view = tk.Toplevel(self.master)
        add_view.geometry("400x400")
        AddTicketView(add_view)

    def gotoViewTicket(self):
        """
        Sets the top level to main menu
        Sets view size and starts to create the view view
        """
        view_view = tk.Toplevel(self.master)
        view_view.geometry("600x350")
        ViewTicketView(view_view)


# ADD Ticket View
class AddTicketView:
    global queue, modes

    def __init__(self, master):
        self.master = master
        self.master.title("Add a ticket")

        # Adding buttons and labels
        self.greeting_label = tk.Label(self.master, text="Create new Tickets")
        self.greeting_label.pack()
        self.current_ticket_label = tk.Label(self.master, text='Current Tickets: ' + str(queue.queueSize()))
        self.current_ticket_label.pack()

        self.name_label = tk.Label(self.master, text='Name: ').pack()
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        self.desc_label = tk.Label(self.master, text='Description: ').pack()
        self.desc_entry = tk.Entry(self.master)
        self.desc_entry.pack()

        self.storeId_label = tk.Label(self.master, text='Store ID: ').pack()
        self.storeId_entry = tk.Entry(self.master)
        self.storeId_entry.pack()

        # Set the radio dials for priority
        self.prio_label = tk.Label(self.master, text='Priority: ').pack()
        self.prio_entry = tk.StringVar()
        for text, mode in modes:
            b = Radiobutton(master, text=modes[text - 1],
                            variable=self.prio_entry, value=mode)
            b.pack()

        self.status_label = tk.Label(self.master, text='Status: ').pack()
        self.status_entry = tk.Entry(self.master)
        self.status_entry.pack()

        self.add = tk.Button(self.master, text="Add Ticket", command=self.addTicket)
        self.add.pack()

    def addTicket(self):
        try:
            ticket = Ticket(self.name_entry.get(), self.desc_entry.get(), self.storeId_entry.get(),
                            self.prio_entry.get(), self.status_entry.get(),
                            datetime.now().replace(microsecond=0))
            queue.addTicket(ticket)
            print(ticket.__repr__())
            self.current_ticket_label.config(text='Current Tickets: ' + str(queue.queueSize()))
            self.clear_entries()
            # add_ticket(conn,ticket)
        except ValueError:
            tkinter.messagebox._show('Value Error: Please try again ', "Store ID must be numbers only")
            self.storeId_entry.delete(0, 'end')

    def clear_entries(self):
        self.name_entry.delete(0, 'end')
        self.storeId_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')
        self.status_entry.delete(0, 'end')
        tkinter.messagebox._show('Ticket Submission', 'Thank you for submitting your ticket')


# View Ticket View

class ViewTicketView:
    global queue

    def __init__(self, master):
        self.master = master
        self.master.title("View Tickets")

        self.greeting_label = tk.Label(self.master, text='View Current Ticket')
        self.greeting_label.pack()
        self.average_ticket_prio_label = tk.Label(self.master, text='Ticket Average: ' + str(self.average_priority()))
        self.average_ticket_prio_label.pack()

        self.Prev_Button = tk.Button(self.master, text="Prev", command=self.prev)
        self.Prev_Button.place(x=5, y=300)
        self.Next_Button = tk.Button(self.master, text='Next', command=self.next)
        self.Next_Button.place(x=560, y=300)
        self.Del_Button = tk.Button(self.master, text='Delete', command=self.delete)
        self.Del_Button.place(x=282, y=300)

        # checks to see if there is a ticket in the queue
        # if not it gives a default message and disables the buttons
        try:
            ticket = queue.currentTicket()
            ticket_view = ticket.__repr__()
            self.ticketView = tk.Label(self.master, borderwidth=20, relief="ridge", text=ticket_view)
            self.ticketView.pack()
        except IndexError:
            ticket_view = "There are no Tickets in the QUEUE.\n " \
                          "Congratulations!!!!!"
            self.ticketView = tk.Label(self.master, borderwidth=20, relief="ridge", text=ticket_view)
            self.ticketView.pack()
            self.disable_buttons()

    def prev(self):
        """
        Sets the ticket to the prev ticket
        updates the ticket view label
        """
        ticket = queue.previousTicket()
        self.ticketView.config(text=ticket.__repr__())

    def next(self):
        """
        Sets the current ticket to the next
        """
        ticket = queue.nextTicket()
        self.ticketView.config(text=ticket.__repr__())

    def delete(self):
        """
        deletes the current ticket from the queue
        changes the view to the ticket at the front of the list
        if the queue is empty displays default setting
        """
        queue.removeTicket()
        if queue._isEmpty:
            self.empty_queue()
        else:
            ticket = queue.currentTicket()
            ticket_view = ticket.__repr__()
            self.ticketView.config(text=ticket_view)
            self.average_ticket_prio_label.config(text=str(self.average_priority()))

    def average_priority(self):
        """
        This calculates the average priority level of the queue
        :return Rounded average of the current queue
        """
        global modes
        priority_dic = {'Low': 1, 'Medium': 2, 'High': 3, 'Emergency': 4}
        total = 0
        for ticket in queue._ticket_list:
            if ticket._priority in priority_dic:
                total += priority_dic[ticket._priority]
        if total == 0:
            return 0
        return round(total / queue._ticket_list.__len__(), 2)

    def empty_queue(self):
        """
        Empty queue
        :return:
        """

        # Example of an inner class.
        # it is called to set the configuration
        def ticket_view():
            var = "There are no Tickets in the QUEUE.\n " \
                  "Congratulations!!!!!"
            return var

        self.ticketView.config(text=ticket_view())
        self.average_ticket_prio_label.config(text=str(self.average_priority()))
        self.disable_buttons()

    def disable_buttons(self):
        """
        disable the buttons when the queue is empty
        """
        self.Prev_Button.config(state='disabled')
        self.Next_Button.config(state='disabled')
        self.Del_Button.config(state='disabled')


def main():
    """
    starts the mail loop for the view
    """
    root = tk.Tk()
    start = MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
