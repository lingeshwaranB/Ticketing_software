class Ticket:
    def __init__(self,id,name,place,time):
        self.id = id
        self.name = name
        self.place = place
        self.time = time

    def display(self):
                print("Ticket_id: ",self.id)
                print("customer_name: ",self.name)
                print("Name of the place: ",self.place)
                print("ticket_timing: ",self.time)

tickets = []

#create
def create():
    id = input("Ticket_id: ")
    name = input("customer_name: ")
    place = input("Name of the place: ")
    time = input("Ticket_timing: ")
#add
    ticket=Ticket(id,name,place,time)

    tickets.append(ticket)
    print("Ticket created successfully")
#delete 
def delete():
    tickets.clear()
    print("Ticket successfully deleted")
    
#display
def display_tickets():
    for ticket in tickets:
        ticket.display()
        break
    else:
        print("Nothing found")
#main program
while True:
    print("-"*10 + "Ticketing_software" + "-"*10)
    print("1. Create Ticket")
    print("2. Display Ticket")
    print("3. Delete Ticket")

    choice = input("Enter your choice: ")
    print("---"*20)
    if choice == "1":
        create()
        print("---"*20)
    elif choice == "2":
        display_tickets()
        print("---"*20)
    elif choice == "3":
        delete()
        print("---"*20)
    else:
        print("---"*20)
        print("**THANK YOU**")
        print("---"*20)
        break
