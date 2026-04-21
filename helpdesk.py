helpdesk_tickets = []

def add_new_ticket():
    user = input("Your name: ")
    problem = input("What is the issue?: ")
    level = input("Priority (Low/Medium/High): ")

    new_ticket = {
        "ticket_id": len(helpdesk_tickets) + 1,
        "user": user,
        "problem": problem,
        "level": level,
        "status": "Open"
    }

    helpdesk_tickets.append(new_ticket)
    print("New ticket successfully added!\n")


def show_all_tickets():
    if not helpdesk_tickets:
        print("No tickets available.\n")
        return

    for t in helpdesk_tickets:
        print(f"ID: {t['ticket_id']}")
        print(f"User: {t['user']}")
        print(f"Issue: {t['problem']}")
        print(f"Priority: {t['level']}")
        print(f"Status: {t['status']}")
        print("-" * 30)


def close_ticket():
    try:
        ticket_number = int(input("Enter ticket ID to close: "))

        for t in helpdesk_tickets:
            if t["ticket_id"] == ticket_number:
                t["status"] = "Closed"
                print("Ticket has been closed.\n")
                return

        print("Ticket not found.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def run_menu():
    while True:
        print("\n--- Help Desk System ---")
        print("1 - Add Ticket")
        print("2 - View Tickets")
        print("3 - Close Ticket")
        print("4 - Exit")

        option = input("Select an option: ")

        if option == "1":
            add_new_ticket()
        elif option == "2":
            show_all_tickets()
        elif option == "3":
            close_ticket()
        elif option == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Try again.\n")


run_menu()