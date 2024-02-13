import datetime
import calendar

def display_menu():
    print("\nCalendar")
    print("1. View events for a day")
    print("2. Add an event for a day")
    print("3. Remove an event for a day")
    print("4. Exit")

def view_events(calendar):
    date = input("Enter the date (YYYY-MM-DD): ")
    if date in calendar:
        events = calendar[date]
        print(f"\nEvents for {date}:")
        for event in events:
            print(f"- {event}")
    else:
        print(f"No events found for {date}.")

def add_event(calendar):
    date = input("Enter the date (YYYY-MM-DD): ")
    event = input("Enter the event: ")
    if date in calendar:
        calendar[date].append(event)
    else:
        calendar[date] = [event]
    print(f"Event added for {date}.")

def remove_event(calendar):
    date = input("Enter the date (YYYY-MM-DD): ")
    if date in calendar:
        events = calendar[date]
        print(f"\nEvents for {date}:")
        for i, event in enumerate(events, 1):
            print(f"{i}. {event}")

        try:
            event_index = int(input("Enter the number of the event to remove:")) - 1
            removed_event = calendar[date].pop(event_index)
            print(f"Removed event: {removed_event}")
        except (ValueError, IndexError):
            print("Invalid input. No event removed.")
    else:
        print(f"No events found for {date}.")

if __name__ == "__main__":
    calendar = {}

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            view_events(calendar)
        elif choice == 2:
            add_event(calendar)
        elif choice == 3:
            remove_event(calendar)
        elif choice == 4:
            print("Exiting..")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
