def response(hey_bob):
    message = hey_bob.strip()

    if message == "":
        return "Fine. Be that way!"

    if message.isupper() and message.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if message.isupper():
        return "Whoa, chill out!"

    if message.endswith("?"):
        return "Sure."

    return "Whatever."