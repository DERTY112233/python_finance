import pyfiglet

title = pyfiglet.figlet_format("TaXeS")
print(title)

def calculate_tax(taxable_income, age):
    # Tax thresholds
    if age < 65:
        threshold = 95750
    elif age < 75:
        threshold = 148217
    else:
        threshold = 165689
    
    # Taxable income after rebate and threshold
    taxable_income -= 17235  # Primary rebate
    if age >= 65:
        taxable_income -= 9444  # Secondary rebate
    if age >= 75:
        taxable_income -= 3145  # Tertiary rebate
    taxable_income = max(0, taxable_income - threshold)
    
    # Tax calculation based on tax brackets
    if taxable_income <= 237100:
        tax = taxable_income * 0.18
    elif taxable_income <= 370500:
        tax = 42678 + (0.26 * (taxable_income - 237100))
    elif taxable_income <= 512800:
        tax = 77362 + (0.31 * (taxable_income - 370500))
    elif taxable_income <= 673000:
        tax = 121475 + (0.36 * (taxable_income - 512800))
    elif taxable_income <= 857900:
        tax = 179147 + (0.39 * (taxable_income - 673000))
    elif taxable_income <= 1817000:
        tax = 251258 + (0.41 * (taxable_income - 857900))
    else:
        tax = 644489 + (0.45 * (taxable_income - 1817000))
    return max(0, tax)

def main():
    try:
        taxable_income = float(input("Enter your taxable income for the year: R "))
        age = int(input("Enter your age: "))
        
        tax = calculate_tax(taxable_income, age)
        
        print("Your estimated tax payable for the year is: R {:.2f}".format(tax))
    except ValueError:
        print("Please enter valid numeric values for taxable income and age.")

if __name__ == "__main__":
    main()
