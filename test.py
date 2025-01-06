from nicegui import ui
import datetime
import random
import socket

# Function to show the current date and time
def show_datetime():
    now = datetime.datetime.now()
    ui.notify(f'Current Date and Time: {now.strftime("%Y-%m-%d %H:%M:%S")}')

# Function to share a joke
def tell_joke():
    joke = "Why don't skeletons fight each other? They don't have the guts!"
    ui.notify(f'Joke: {joke}')

# Function to show a motivational quote
def show_quote():
    quote = "The only way to do great work is to love what you do. - Steve Jobs"
    ui.notify(f'Motivational Quote: {quote}')

# Function to show a random number between 1 and 100
def random_number():
    number = random.randint(1, 100)
    ui.notify(f'Random Number: {number}')

# Function to show the user's IP address
def show_ip():
    ip_address = socket.gethostbyname(socket.gethostname())
    ui.notify(f'Your IP Address: {ip_address}')

# Function to greet the user with a "Hello" message
def greet_user():
    ui.notify("Hello! Welcome to the NiceGUI app!")

# Function to calculate the square of a number
def square_number():
    num = 5
    square = num ** 2
    ui.notify(f'The square of {num} is {square}')

# UI setup with tabs
with ui.tabs():
    with ui.tab('Datetime'):
        ui.button('Show Current Date and Time', on_click=show_datetime)

    with ui.tab('Joke'):
        ui.button('Tell Me a Joke', on_click=tell_joke)

    with ui.tab('Quote'):
        ui.button('Show Motivational Quote', on_click=show_quote)

    with ui.tab('Random Number'):
        ui.button('Generate Random Number', on_click=random_number)

    with ui.tab('IP Address'):
        ui.button('Show My IP Address', on_click=show_ip)

    with ui.tab('Greeting'):
        ui.button('Greet Me', on_click=greet_user)

    with ui.tab('Square'):
        ui.button('Calculate Square of 5', on_click=square_number)

# Run the app on host and port 8080
ui.run(host="0.0.0.0", port=8080)
