"""Q18: Gross = basic + bonus; tax is a percentage of gross."""
def employee_salary(name, basic, bonus_percentage, tax_percentage):
    if not name.strip() or basic < 0 or not 0 <= bonus_percentage <= 100 or not 0 <= tax_percentage <= 100:
        raise ValueError("Invalid employee name, salary or percentages")
    bonus = basic * bonus_percentage / 100
    gross = basic + bonus
    tax = gross * tax_percentage / 100
    return {"name": name, "bonus": round(bonus, 2), "gross": round(gross, 2), "tax": round(tax, 2), "net": round(gross - tax, 2)}
def main():
    print("Enter details for five employees")
    for i in range(1, 6):
        print(f"\nEmployee {i}")
        while True:
            try:
                result = employee_salary(input("Name: ").strip(), float(input("Basic salary: ")),
                                         float(input("Bonus %: ")), float(input("Tax %: ")))
                break
            except ValueError as e: print("Invalid input; retry employee:", e)
        for key, value in result.items(): print(f"{key}: {value}")
if __name__ == "__main__": main()
