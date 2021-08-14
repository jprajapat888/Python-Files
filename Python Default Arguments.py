def greet(name, msg="Good Morning!"):
    """
    This function greets to the person with the provided message.
    if the message is not provided, it defaults to "Good Morning!"
    """

    print("Hello", name + ',' + msg)

greet("Kate")
greet("Bruce, How do you do?")