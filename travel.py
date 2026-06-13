passenger_name:"maya"
destination:"Brazil"
ticket_price:1130
number_of_tickets:1
is_available:True
print("passenger name:",passenger_name)
print("destination:",destination)
print("ticket price:Rs", ticket_price)
print("number of tickets:",number_of_tickets)
print("tickets available?:",is_available)
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
total_cost = ticket_price * number_of_tickets
discount = 25
final_cost = total_cost - discount
print("\ntotal cost:Rs",total_cost)
print("Discount :Rs", discount)
print("final cost :Rs", final_cost)
print("double ticket price :Rs", ticket_price * 2)
print("ticket price after Rs50 increase :Rs", ticket_price + 50)
print("half ticket_price :Rs", ticket_price/2)
print("\nIs ticket price over 1000?", ticket_price < 1000)
print("Are more than 2 tickets booked?", number_of_tickets > 2)
print("Is destination Brazil?", destination==Brazil)
print("is final_cost more than Rs2000?", final_cost > 2000)
travel_message = passenger_name + "is travveling to" + destination + "."
print("\nTravel message :", travel_message)
print("Desination in uppercase:", destination.upper())
print("passenger name in lowercase:", passenger_name.lowercase())
print("First letter of destination:", destination[0])
print("length of passenger name:", len(passenger_name))
morning_ticket_price = 1000
evening_ticket_price = 1140
print("\n Before swapping:")
print("morning ticket price:Rs", morning_ticket_price)
print("evening ticket price:Rs", evening_ticket_price)
morning_ticket_price,evening_ticket_price = evening_ticket_price,morning_ticket_price
print("\nAfter swapping:")
print("morning ticket price :RS", morning_ticket_price)
print("evening ticket price :Rs", evening_ticket_price)
print("\n=5")
print("TRAVEL TICKET SUMMARY")
print("5")
print("passenger name:", passenger_name)
print("destination:", destination)
print("Tickets booked:", number_of_tickets)
print("Final amount to pay:Rs", final_cost)
print("Booking confirmed: Rs", is_available)