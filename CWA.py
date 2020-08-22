import time

""" Give integer for number of units completed """
num_units = int(input("Number of Units Taken:  "))

def CWA(num_units):
    weight = 0
    creds = 0

    for ii in range(1, num_units + 1):
        time.sleep(0.3)
        unit_mark = int(input("Enter Unit Mark w/o %:  "))
        print("~~~~~")
        time.sleep(0.3)
        unit_credit = int(input("Enter Unit Credit: "))
        print("~~~~~")

        unit_weight = unit_credit * unit_mark
        weight += unit_weight
        creds += unit_credit
    
    CWA = weight / creds
    US_GPA = ((CWA + 10) / 20) - 1
    AUS_GPA = US_GPA + 3

    CWA_display = print("Current CWA: ", str(round(CWA, 1)))
    GPA_display = print("Approx US 4.0 Scale GPA:", str(round(US_GPA, 2)))
    AUSGPA_display = print("Approx AUS 7.0 Scale GPA:", str(round(AUS_GPA, 3)))

    println = str(CWA_display) + str(GPA_display) + str(AUSGPA_display)

    return println


#program driver
if __name__ == "__main__":
    CWA(num_units)