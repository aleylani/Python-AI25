import argparse    # argument parsing via CLI (comand line interface / kommando tolken)

# läs mer om argparse via https://www.datacamp.com/tutorial/python-argparse


# 1. Skapa ett parser-objekt som är beredd på att ta emot argument från CLI
parser = argparse.ArgumentParser(description='A Python script that accepts arguments from the CLI, and greets the user.')

# 2. Lägg till de argument som vi vill kunna ta emot från CLI

# mandatory argument
parser.add_argument('--name', type=str, required=True, help='Your name (str)')

# optional argument

parser.add_argument('--age', type=float, default=25, help='Your age (float)')
parser.add_argument('--city', type=str, default=None, help='The city you live in (str)')

# 3. Parsa/importera argumenten som användaren anger, och lägg in allt i variabeln args

args = parser.parse_args()

print(f'args.name har fått värdet {args.name}')
print(f'args.age har fått värdet {args.age}')
print(f'args.city har fått värdet {args.city}')

def greet(name: str, age: float = None, city: str = 'Unknown'):

    print(f'Hello {name}!')

    if age:                                # detta kommer evalueras till False, om vi inte ändrar default-värdet av age
                                           # by default har age värdet None, och satsen evalueras därför till False
        print(f'You are {age} years old.')

    print(f'You live in {city}.')

greet(name = args.name, age = args.age, city = args.city)


