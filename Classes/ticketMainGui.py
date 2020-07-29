import tkinter as tk
from datetime import datetime
from tkinter.ttk import *
# create the ticket queue to start the program
from Classes.ticket import Ticket
from Classes.ticket_queue import TicketsQueue

queue = TicketsQueue()
date = datetime.now()
test = Ticket("1", "ththt", "this is", "kdfadf", "emergency", date)
queue.addTicket(test)


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
        addview = tk.Toplevel(self.master)
        AddTicketView(addview, self.q)

    def gotoViewTicket(self):
        viewView = tk.Toplevel(self.master)
        ViewTicketView(viewView, self.q)


class AddTicketView:
    def __init__(self, master, q):
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
        self.prio_entry = tk.Entry(self.master)
        self.prio_entry.pack()

        self.status_label = tk.Label(self.master, text='Status: ').pack()
        self.status_entry = tk.Entry(self.master)
        self.status_entry.pack()

        self.date_label = tk.Label(self.master, text='Date: ').pack()
        self.date_entry = tk.Entry(self.master)
        self.date_entry.pack()

        self.add = tk.Button(self.master, text="Add Ticket", command=lambda queue=q: self.addTicket(queue))
        self.add.pack()

    def addTicket(self, q):
        global test
        ticket = Ticket(self.name_entry.get(), self.desc_entry.get(), self.storeId_entry.get(), self.prio_entry.get(),
                        self.status_entry.get(), self.date_entry.get())
        q.addTicket(ticket)
        print(ticket.__repr__())
        self.current_ticket_label.config(text='Current Tickets: ' + str(queue.queueSize()))


class ViewTicketView:
    def __init__(self, master, q):
        self.master = master
        self.master.title("Add a ticket")

        self.greeting_label = tk.Label(self.master, text="Create new Tickets")
        self.greeting_label.pack()


def main():
    root = tk.Tk()
    start = MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
