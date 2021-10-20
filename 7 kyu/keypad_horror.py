def computer_to_phone(numbers):
    ans = ""
    for number in numbers:
        if number == "1":
            ans += "7"
        elif number == "2":
            ans += "8"
        elif number == "3":
            ans += "9"
        elif number == "7":
            ans += "1"
        elif number == "8":
            ans += "2"
        elif number == "9":
            ans += "3"
        else:
            ans += str(number)
    return ans