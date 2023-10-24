from flask import Flask
import random

app = Flask(__name__)



@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert} ?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective,noun):
    return f'Once upon a time there was a {noun}, the {noun} was very {adjective}, and used that to their advantage to get free food from the food truck at Dominican.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1,number2):
    if number1.isdigit() and number2.isdigit():
        temp = int(number1) * int(number2)
        return f'{number1} times {number2} is {temp}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'
    
@app.route ('/sayntimes/<word>/<n>')
def sayntime(word,n):
    if n.isdigit():
        n = int(n)
        temp = ""   
        for _ in range(n):
            temp+=word
        return temp
    else: 
        return'Invalid input. Please try again by entering a word and a number!'
@app.route('/dicegame')
def dicegame():
    temp = random.randint(1,6)
    if temp == 6:
        return f'You rolled a {temp}. You Win!'
    else: return f'You rolled a {temp}. You Lost!'
    """return f'You rolled a {temp}'"""




@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

if __name__ == '__main__':
    app.run(debug=True)

