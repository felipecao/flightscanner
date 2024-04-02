from sheety_client import SheetyClient

sheety_client = SheetyClient()

print('Welcome to the Flight Club!')
print("Rule #1: don't talk about the flight club")

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

while True:
    email = input('What is your e-mail? ')
    email_confirmation = input('Please type your e-mail again for confirmation. ')

    if email != email_confirmation:
        print('Please use the same email address for both questions. Please try again.')
    else:
        break


print('Please wait...')
response = sheety_client.add_new_customer(first_name, last_name, email)

if response.status_code == 200:
    print("All set! You're in the club!")
else:
    print(f"Something went wrong, response code is {response.status_code}")


