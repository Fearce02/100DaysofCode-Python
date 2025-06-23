# You can also nest a list and a dictionary into another dictionary.

captials = {
    "India" :"Delhi",
    "France" :"Paris",
    "Ireland" :"Dublin"
}

#Nested list in dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "India" : ["Red-Fort", "India-Gate", "Qutub-Minar"]
}

#Print india-gate from travel log

india_gate = travel_log["India"][1]
print(india_gate)

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

new_travel_log = {

    "India": {
        "places_visited" : ["Red-Fort", "India-Gate", "Qutub-Minar"],
        "total_visits" : 5
    },
    "France": {
         "places_visited" : ["Paris", "Lille", "Dijon"],
         "total_visits": 12
    }
}

dijon = new_travel_log["France"]["places_visited"][2]
print(dijon)