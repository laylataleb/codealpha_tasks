import json
import random
from nltk.chat.util import Chat, reflections
from hangman import play_hangman 
# from playsound import playsound  

# Loading data from JSON file
with open('chatbot_data.json', 'r') as file:
    data = json.load(file)

# Extracting data from chatbot_data.json
pairs = []
for category in ['greetings', 'farewells']:
    for entry in data[category]:
        pairs.append([entry['pattern'], entry['responses']])

jokes = data['jokes']
quotes = data['quotes']

# Function to play sounds
#
#    playsound('greeting.mp3')

#def play_joke_sound():
#    playsound('joke.mp3')

# Initialize the chatbot 
def chatbot():
    print("ChatBot: Hi, I'm ChatBot! How can I help you today?")
    #play_greeting_sound()
    chat = Chat(pairs, reflections)
    #chat.converse()

    while True:
        user_input = input("You: ").lower()

        if "joke " in user_input or "laugh " in user_input: 
            print(f"ChatBot: {random.choice(jokes)}")
            #play_joke_sound()

        elif "quote" in user_input or "motivate" in user_input:
            print(f"ChatBot: {random.choice(quotes)}")

        elif "hangman" in user_input:
            play_hangman() 

        elif user_input.lower() in ["quit", "exit", "bye"]:
            print("ChatBot: Goodbye!")
            break

        else:
            response = chat.respond(user_input)
            if response:
                print(f"ChatBot: {response}")
            else:
                print("ChatBot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()
