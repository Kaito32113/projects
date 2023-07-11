def main():
    print("This program converts INR to US dollars")
    print()

    rupees = eval(input("Enter amount in rupees: "))

    dollars = convert_to_dollars(rupees)

    print("That is" , dollars, "dollars. ")

convert_to_dollars = lambda dollars: dollars * 0.012

main()