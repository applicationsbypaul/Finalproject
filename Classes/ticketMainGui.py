import tkinter as tk
from datetime import datetime
from tkinter.ttk import *
# create the ticket queue to start the program
from Classes.ticket import Ticket
from Classes.ticket_queue import TicketsQueue

queue = TicketsQueue()
date = datetime.now().replace(microsecond=0)
test = Ticket("1", "ththt", "this is",
              "hdfghdfghdfghdfghdfgh dfghdhfghdfghdfg\nsdfgsfhjfdfghdfgsdfgh",
              "emergency", date)
# queue.addTicket(test)
priority = {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Emergency'}


class MainMenu:
    global queue

    def __init__(self, master):
        self.q = queue
        self.master = master
        self.master.title("Ticket Queue")
        self.master.greetingLabel = tk.Label(self.master, text="Welcome to Ticket Creator")
        self.master.greetingLabel.pack()
        self.master.addTicketButton = tk.Button(self.master, text="Add New Ticket", bg="green", fg="white",
                                                command=self.gotoAddTicket)
        self.master.addTicketButton.pack()

        self.master.viewTicketButton = tk.Button(self.master, text="View Tickets", bg="blue", fg="white",
                                                 command=self.gotoViewTicket)
        self.master.viewTicketButton.pack()

    def gotoAddTicket(self):
        add_view = tk.Toplevel(self.master)
        add_view.geometry("400x400")
        AddTicketView(add_view)

    def gotoViewTicket(self):
        view_view = tk.Toplevel(self.master)
        view_view.geometry("600x350")
        ViewTicketView(view_view)


class AddTicketView:
    global queue, priority

    def __init__(self, master):
        self.master = master
        self.master.title("Add a ticket")

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

        self.prio_label = tk.Label(self.master, text='Priority: ').pack()
        modes = [
            (1, "Low"),
            (2, "Medium"),
            (3, "High"),
            (4, "Emergency")
        ]

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
        ticket = Ticket(self.name_entry.get(), self.desc_entry.get(), self.storeId_entry.get(),
                        self.prio_entry.get(), self.status_entry.get(),
                        date.now().replace(microsecond=0))
        queue.addTicket(ticket)
        print(ticket.__repr__())
        self.current_ticket_label.config(text='Current Tickets: ' + str(queue.queueSize()))

    def average_priority(self):
        total = 0
        for prio in queue._ticket_list:
            ticket = queue._ticket_list[prio]
            total += ticket._priority
        return round(total / queue._ticket_list.__len__(), 2)


class ViewTicketView:
    global queue

    def __init__(self, master):
        self.master = master
        self.master.title("View Tickets")

        self.greeting_label = tk.Label(self.master, text="View Current Ticket")
        self.greeting_label.pack()

        self.Prev_Button = tk.Button(self.master, text="Prev", command=self.prev)
        self.Prev_Button.place(x=5, y=300)
        self.Next_Button = tk.Button(self.master, text='Next', command=self.next)
        self.Next_Button.place(x=560, y=300)

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
            self.Prev_Button.config(state='disabled')
            self.Next_Button.config(state='disabled')

    def prev(self):
        ticket = queue.previousTicket()
        self.ticketView.config(text=ticket.__repr__())

    def next(self):
        ticket = queue.nextTicket()
        self.ticketView.config(text=ticket.__repr__())


def main():
    root = tk.Tk()
    start = MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
