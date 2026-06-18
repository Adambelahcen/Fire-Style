def line_up(name, number):
    number = str(number)

    sentence = name + "," + " " + "you are the" + " " + number + "ordinal" + " customer we serve today. Thank you!"

    if number[-1] == "1" and not number.endswith("11"):
        return sentence.replace("ordinal", "st")
    if number[-1] == "2" and not number.endswith("12"):
        return sentence.replace("ordinal", "nd")
    if number[-1] == "3" and not number.endswith("13"):
        return sentence.replace("ordinal", "rd")
    else:
        return sentence.replace("ordinal", "th")