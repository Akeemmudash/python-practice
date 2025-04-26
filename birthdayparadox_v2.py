"""Birthday Paradox Simulation, by Al  Sweigart al@inventwithoyhton.com
Explore the surpising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

from random import randint
from datetime import timedelta, date


def main():
    try:
        print("""Birthday Paradox, by Akeem Mudashiru akeemmudash@gmail.com

The Birthday Paradox shows that in group of N people, the odds
that two of have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random simulation)
to explore this concept.

(It's not actually a paradox, it's just a surprisingly result.) 
                    
    """)
        MONTHS = ("Jan", "Feb", "Mar", "Apr", "May","Jun","Jul"
                    , "Aug", "Sep", "Oct", "Nov", "Dec"
                    )
        num_simulation_match = 0
        while True:
            print("How many birthdays shall I generate? (Max 100)")
            num_of_bdays = input("> ")
            num_of_bdays_int = int(num_of_bdays)
            if num_of_bdays.isdecimal() and (0 < num_of_bdays_int <= 100):
                    break
        print() 
        print("Here are {} birthdays:".format(num_of_bdays_int))
        birthdays = get_rand_bdays(num_of_bdays_int)
        for i, birthday in enumerate(birthdays):
            bday_month = MONTHS[int(birthday.month) - 1]
            print("{:<3} {:>2}".format(bday_month, birthday.day), end="")
            if i != len(birthdays) - 1:
                print(", ", end="")
        print()
        print()
        match = getmatch(birthdays)
        if match != None:
            monthName = MONTHS[birthday.month - 1]
            print("In this simulation, multiple people have a birthday on {} {}".format(monthName, birthday.day))
        else:
            print("There are no matches in this simulation")  
        
        print()
        print("Generating {} random birthdays 100,000 times...".format(num_of_bdays_int))
        input("Press Enter to begin...")
    
        for i in range(100_000):
            if i % 10_000 == 0:
                print("{} simulations run...".format(i))
            if getmatch(birthdays) != None:
                num_simulation_match += 1

        print("100,000 simulations run...")

        probability = round(num_simulation_match / 100_000 * 100.0,2)

        print(f"""Out of 100,000 simulations of {num_of_bdays} people, there was a
matching birthday in that group {num_simulation_match} times. This means
that {num_of_bdays} people have a {probability} % chance of
having a matching birthday in their group.
That's probably more than you would think!
""")
    except (KeyboardInterrupt, EOFError):
        print("Good bye!")

def get_rand_bdays(num_of_bdays):
    ist_bday_of_year = date(2001, 1, 1)
    birthdays = []

    for i in range(num_of_bdays):
        random_offset_bday = timedelta(randint(0, 364))
        birthday = random_offset_bday + ist_bday_of_year
        birthdays.append(birthday)
    return birthdays  
    

def getmatch(birthdays):
     if birthdays == set(birthdays):
          return None
     
     for a, birthdayA in enumerate(birthdays):
         for  birthdayB in birthdays[a + 1:]:
              if birthdayA == birthdayB:
                   return birthdayA
       
    
            
            
      
if __name__ == "__main__":
     main()