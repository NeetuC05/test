#import the necessary SymPy libraries
from sympy.logic.boolalg import And, Or, Not
from sympy.abc import x, y

#define basic predicates as symbols
IsCloudy = lambda day: f"{day} is cloudy"
IsHumid = lambda day: f"{day} is humid"
WillRain = lambda day: f"It will rain on {day}"

#facts
facts = {
    "Monday": True,   # Monday is cloudy
    "Tuesday": True,  # Tuesday is humid
    "Wednesday": False, # Wednesday is neither cloudy nor humid
    "Thursday": True,  # Thursday is cloudy
    "Friday": True,    # Friday is humid
}

#Rule (First-order-logic): if it is cloudy and humid, then it will rain
#rule: IsCloudy(x) AND IsHumid(x) => WillRain(x)
def rule(day):
    is_cloudy = facts.get(day, False)  # Check if the day is cloudy
    is_humid = facts.get(day, False)   # Check if the day is humid
    # Assuming we have a separate fact for humidity
    if day in ["Tuesday", "Friday"]:  # Let's say these days are humid
        is_humid = True
    if is_cloudy and is_humid:  # If both conditions are true
        return WillRain(day)  # Then it will rain

#query for the weather on a given day
def query(day):
    #check if the rule holds for the given day
    if rule(day):
        return f"{day}: It will rain"
    else:
        return f"{day}: It will not rain"
    
#running queries
print(query("Monday"))    # should return "Monday: It will rain"
print(query("Tuesday"))   # should return "Tuesday: It will rain"
print(query("Wednesday")) # should return "Wednesday: It will not rain"
print(query("Thursday"))  # should return "Thursday: It will rain"
print(query("Friday"))    # should return "Friday: It will rain"

#generalized query for all days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    print(query(day))
