def average(running_total, count):
    print()
    new_total = running_total
    total_numbers = count
    selection = input("Enter an integer (Q or q to quit): ")

    def isfloat(selection):
        try:
            float(selection)
            return True
        except ValueError:
            return False

    if isfloat(selection) or selection.isdigit():
        new_total += float(selection)
        total_numbers += 1
        average(new_total, total_numbers)
    if selection == "Q" or selection == "q":
        if total_numbers == 0:
             print("Not enough data to calculate")
        else:
            total_average = new_total / total_numbers
            print(f"The average of the numbers you entered is {total_average}")
            exit()
    else:
        average(new_total, total_numbers)

def main():
    print()
    print("This program finds the average of the integers you enter.")
    average(0, 0)

main()

