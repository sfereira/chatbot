# Python Chatbot

### Description

* This is a simple python chatbot that uses a basic set of pre-defined messages and probability to respond to user input.
* The chatbot uses natural language processing techniques to recognize certain words in a user's message and respond accordingly.

### Requirements

To run this Python chatbot, you will need to have the following:

1. `Python 3.x` installed
2. The `re` module
3. The `random` module

### Usage

1. Clone or download the repository.
2. Open the terminal or command prompt and navigate to the project directory.
3. Run the command `python chatbot.py`.
4. Type a message to the chatbot and press enter and the chatbot will respond to your message.
5. The chatbot will ask for user input, and will continue to respond until the program is stopped or exited.

### How it works

* The chatbot works by first taking in user input and splitting it into individual words using a regular expression.
* The words are then compared to a set of recognised words to pre-defined messages.
* The probability of a message being the correct response is calculated by dividing the number of recognised words in the user input by the total number of recognised words in the pre-defined message.
* If a required word is not present in the user input, the probability of that message being the correct response is set to 0.
* The chatbot then selects the message with the highest probability as the response to the user input.
* If no message has a probability greater than 1, a default "unknown" message is returned.

