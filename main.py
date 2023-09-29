class Ticket:
    def __init__(self, movie_name, ticket_price, num_tickets, language="Geo"):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.num_tickets = num_tickets
        self.language = language

    def __str__(self):
        return f"{self.movie_name}, {self.num_tickets} tickets left at {self.ticket_price} {self.language}"

    def __lt__(self, other):
        return self.num_tickets < other.num_tickets

    def __eq__(self, other):
        return self.num_tickets == other.num_tickets


class User:
    def __init__(self, buyer_name, balance_amount):
        self.buyer_name = buyer_name
        self.__balance_amount = balance_amount

    def __str__(self):
        return f"{self.buyer_name} has {self.__balance_amount} in their account"

    def buy_ticket(self, ticket, num_tickets):
        total_cost = ticket.ticket_price * num_tickets
        if total_cost <= self.__balance_amount and num_tickets <= ticket.num_tickets:
            self.__balance_amount -= total_cost
            ticket.num_tickets -= num_tickets
            print(f"You bought {num_tickets} tickets to {ticket.movie_name}")
        elif total_cost > self.__balance_amount:
            print("You do not have enough funds to make this purchase.")
        else:
            print("There are not enough tickets available to complete your purchase.")

    def deposit(self, amount):
        self.__balance_amount += amount


# Creating objects for testing
ticket1 = Ticket("Avengers: Endgame", 10, 100, "ENG")
ticket2 = Ticket("The Lion King", 8, 50)

user1 = User("John", 50)
user2 = User("Sarah", 20)

# Testing __str__() method
print(ticket1)
print(user1)

# Testing buy_ticket() method
user1.buy_ticket(ticket1, 2)
user2.buy_ticket(ticket2, 10)
user1.buy_ticket(ticket1, 20)

# Testing deposit() method
user1.deposit(30)
print(user1)

# Testing comparison operator overloading
if ticket1 > ticket2:
    print(f"There are more tickets left for {ticket1.movie_name} than {ticket2.movie_name}")
elif ticket1 < ticket2:
    print(f"There are more tickets left for {ticket2.movie_name} than {ticket1.movie_name}")
else:
    print(
        f"The number of tickets left for {ticket1.movie_name} is equal to the number of tickets left for {ticket2.movie_name}")


# Polymorphism example
def increase_tickets(ticket):
    ticket.num_tickets += 10
    print(f"The number of tickets for {ticket.movie_name} has been increased to {ticket.num_tickets}")


increase_tickets(ticket1)
