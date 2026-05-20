import json

from datetime import date

# Centralized filename makes it easy to change storage location later
FILE_NAME = "applications.json"


def load_applications():

    # Return an empty list if the file does not exist or contains invalid JSON
    try:

        with open(FILE_NAME, "r") as file:

            return json.load(file)
        
    except FileNotFoundError:

        return []
    
    except json.JSONDecodeError:

        return []


def save_applications(applications):

    with open(FILE_NAME, "w") as file:

        # Persist the entire application list after any add, update, or delete operation
        json.dump(applications, file, indent=4)


def choose_status():

    # Restrict status values to a predefined list for consistency
    statuses = [

        "Applied",

        "Interview Scheduled",

        "Interviewed",

        "Rejected",

        "Offer Received"

    ]

    print("\nChoose status:")

    for index, status in enumerate(statuses, start=1):

        print(f"{index}. {status}")

    try:

        choice = int(input("Enter status number: "))

        if choice < 1 or choice > len(statuses):

            print("Invalid status. Defaulting to Applied.")

            return "Applied"

        # Convert the user's menu selection into the matching status string
        return statuses[choice - 1]

    except ValueError:

        print("Invalid input. Defaulting to Applied.")

        return "Applied"


def add_application():
    
    company = input("Company name: ")

    position = input("Position title: ")
    
    location = input("Location: ")

    # Automatically record the current date when an application is created
    date_applied = str(date.today())

    status = choose_status()

    link = input("Job link: ")

    notes = input("Notes: ")

    # Store each application as a dictionary so related details stay grouped together
    application = {

        "company": company,

        "position": position,

        "location": location,

        "date_applied": date_applied,

        "status": status,

        "link": link,

        "notes": notes

    }

    # Load existing records before adding the new application
    applications = load_applications()

    # Append the new application to the in-memory list
    applications.append(application)

    save_applications(applications)

    print("Application added successfully!")


def view_applications():

    applications = load_applications()

    if not applications:

        print("No applications found.")

        return

    # Enumerate provides user-friendly numbering starting at 1 instead of 0
    for index, app in enumerate(applications, start=1):

        # .get() prevents KeyError if older records are missing newer fields
        print(f"""
              
             Application #{index}


             Company: {app.get("company", "N/A")}

             Position: {app.get("position", "N/A")}

             Location: {app.get("location", "N/A")}

             Date Applied: {app.get("date_applied", "N/A")}

             Status: {app.get("status", "N/A")}           

             Link: {app.get("link", "N/A")}

             Notes: {app.get("notes", "N/A")}


             --------------------

             """)


def search_applications():

    # Convert search input to lowercase to support case-insensitive matching
    search_term = input("Search company or position: ").lower()

    applications = load_applications()

    # Track whether at least one match was found
    found = False

    for index, app in enumerate(applications, start=1):

        # Search both company and position fields to improve discoverability
        if search_term in app.get("company", "").lower() or search_term in app.get("position", "").lower():
            
            print(f"""
              
             Application #{index}


             Company: {app.get("company", "N/A")}

             Position: {app.get("position", "N/A")}

             Location: {app.get("location", "N/A")}

             Date Applied: {app.get("date_applied", "N/A")}

             Status: {app.get("status", "N/A")}           

             Link: {app.get("link", "N/A")}

             Notes: {app.get("notes", "N/A")}


             --------------------
 
             """)
            
            found = True

    if not found:

        print("No matching applications found.")


def update_status():

    applications = load_applications()

    # Display current applications so the user can choose the correct record to update
    view_applications()

    if not applications:

        return

    try:

        app_number = int(input("Enter application number to update: "))

        if app_number < 1 or app_number > len(applications):

            print("Invalid application number.")

            return

        new_status = choose_status()

        # Convert the displayed application number into a valid list index
        applications[app_number - 1]["status"] = new_status

        save_applications(applications)

        print("Status updated successfully!")

    except ValueError:

        print("Please enter a valid number.")


def delete_application():

    applications = load_applications()

    view_applications()

    if not applications:

        return

    try:

        app_number = int(input("Enter application number to delete: "))

        if app_number < 1 or app_number > len(applications):

            print("Invalid application number.")

            return

        # Remove and return the selected application in a single operation
        deleted_app = applications.pop(app_number - 1)

        save_applications(applications)

        print(f"Deleted application for {deleted_app.get('company', 'N/A')}.")

    except ValueError:

        print("Please enter a valid number.")


def filter_by_status():

    applications = load_applications()

    if not applications:

        print("No applications found.")

        return

    # Reuse the status menu to ensure filtering uses valid status values
    selected_status = choose_status()

    found = False

    for index, app in enumerate(applications, start=1):

        # Compare statuses case-insensitively for reliability
        if app.get("status", "").lower() == selected_status.lower():

            print(f"""
              
             Application #{index}


             Company: {app.get("company", "N/A")}

             Position: {app.get("position", "N/A")}

             Location: {app.get("location", "N/A")}

             Date Applied: {app.get("date_applied", "N/A")}

             Status: {app.get("status", "N/A")}           

             Link: {app.get("link", "N/A")}

             Notes: {app.get("notes", "N/A")}


             --------------------

             """)

            found = True

    if not found:

        print(f"No applications found with status: {selected_status}")


def main():

    # Keep the application running until the user explicitly chooses to exit
    while True:

        print("""
              
        Job Application Tracker

        1. Add application
              
        2. View all applications
              
        3. Search applications
              
        4. Update application status
              
        5. Delete application
              
        6. Filter by status
              
        7. Exit
              
        """)

        choice = input("Choose an option: ")

        if choice == "1":

            add_application()

        elif choice == "2":

            view_applications()

        elif choice == "3":

            search_applications()

        elif choice == "4":

            update_status()

        elif choice == "5":

            delete_application()

        elif choice == "6":

            filter_by_status()

        elif choice == "7":

            print("Goodbye!")

            break

        else:

            print("Invalid choice. Please try again.")


# Only run the menu loop when this file is executed directly
if __name__ == "__main__":

    main()