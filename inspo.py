class MessagePrinter:
    def __init__(self):
        self.message = '''Tired of being broke? Act shamelessly. 
The incentives you get from trial and error are greater than the cost of waiting for things to be perfect.'''

    def display_message(self):
        print(self.message)

# Create an instance of the class and call the method
printer = MessagePrinter()
printer.display_message()
