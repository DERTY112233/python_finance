import pyfiglet

title = pyfiglet.figlet_format("FinancePy")

print(title)

decision = input("""[+] WOULD YOU LIKE TO CALCULATE
                 1) MONTHLY INTEREST
                 2) ANUAL INTEREST
                 --->>>> """)

def calc_for_year():
    print("please input the following:")
    principle = input("[+] PRINCIPLE: R ")
    interest = input("[+] INTEREST: ")
    principle = float(principle)
    interest = float(interest)
    final_result = principle*(interest/100)
    final_result = final_result.__round__(3)
    print(f"[+] HERE IS THE RESULT OF THE YEARLY INTERST CALCULATION:   R {final_result}")
    
    
def calc_for_monthly():
    print("please input the following:")
    principle = input("[+] PRINCIPLE: R ")
    interest = input("[+] INTEREST: ")
    principle = float(principle)
    interest = float(interest)
    final_result = principle*(interest/12)
    final_result = final_result.__round__(3)
    print(f"[+] HERE IS THE RESULT OF THE MONTHLY INTERST CALCULATION:   R{final_result}")


match decision:
    case "1":
        calc_for_monthly()
    case "2":
        calc_for_year()
