import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rILiVe8JUyn2e4N7qQSHKHs5uNGwPP7Y"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    print("\nWhat metric system do you want to use?")
    print("For kilometers, enter: K")
    print("For miles, enter: M")
    
    while True:
        unit = input("Your Choice: ")
        if unit == "K" or unit == "k":
            unit = "Kilometers"
            break
        elif unit == "M" or unit == "m":
            unit = "Miles"
            break
        else:
            print("Invalid unit!")

    print("\nDistance Unit will be {}".format(unit))
    print("\n")
        
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    print("URL: " + (url))
    json_data = requests.get(url).json()
    #route_json = json_data["route"]
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print(json_data["route"])
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        if unit == "Kilometers":
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        else:
            print("Miles:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        #print("Fuel Used (Ltr): " + str("{:.2f}".format(json_data["route"]["fuelUsed"]*3.78)))
        print("Uses Highway?: " + str(json_data["route"]["hasHighway"]))
        print("Has Dirt Road?: " + str(json_data["route"]["hasUnpaved"]))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            if unit == "Kilometers":
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            else:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " miles)"))
            print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")





