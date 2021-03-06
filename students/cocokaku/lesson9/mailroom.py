#!/usr/bin/python3
from donors import Donors

DONOR_DB = Donors({
    "William Gates, III": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Colleen Kaku": [50000, 1000000, 1000000]
    })


def send_thank_you(db):
    """Add a donor/donation and print out a thank you letter"""
    # loop for user input: donor name, or list, or quit
    while True:
        name = input("\nDonor Full Name (type 'list' for donor list or 'q' to quit): ")
        if name in ('q', 'quit'):
            return
        if name == 'list':
            print(db.list_donors())
            continue
        # if name == donor name:
        #   loop for user to input valid donation amount
        while True:
            amount = input("Donation amount (type 'q' to quit): ")
            if amount in ('q', 'quit'):
                return
            try:
                db.add_donation(name, amount)
            except ValueError:
                print('Invalid input, try again')
            else:
                break
        print('\n' + db.thank_you_letter(name))


def create_a_report(db):
    """Print a summary of donors and amounts donated to screen"""
    print("\n"+db.summary_report())


def send_all_letters(db):
    """Write thank you letters to all donors to text files, filename = <donor_name>.txt"""
    dir_name = input("Output directory ('.' for current dir): ")
    db.send_all_letters(dir_name)


def main_menu_error(_):
    print("Invalid choice, try again")


def quit_program(_):
    quit()


def main():
    """Main menu for mailroom program"""
    switch_menu_dict = {
        "1": send_thank_you,
        "2": create_a_report,
        "3": send_all_letters,
        "q": quit_program,
        "quit": quit_program
        }
    while True:
        print("\nMAIN MENU")
        print("   1 = Send a Thank You")
        print("   2 = Create a Report")
        print("   3 = Send Letters to Everyone")
        print("   q = Quit")
        choice = input("   ? ")
        switch_menu_dict.get(choice, main_menu_error)(DONOR_DB)


if __name__ == '__main__':
    main()
