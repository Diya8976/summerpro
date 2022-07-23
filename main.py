import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    #response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Harry potter',['J.K. Rowlings'], "Perks of being a wallflower",["Stephen Chbosky"],"Ender's game",["Orson Scott Card"],
                "The Hobbit",["Michael Green"], "The Giver",["lois lowry",],"Hannibal",[ "Thomas Harris"], "The da vinci code",["Dan Brown "], 
                "Alchemist ",["Paulo Coelho"],"To kill a mocking bird ",["Harper Lee"], "The Brethren ",[ "John Grisham"], 
                "Good Omens ",["Neil Gaiman"], "After Dark ",["Jayne Castle"],"Kaleidoscope",["June Stepansky"], "Stardust",["Neil Gaiman"],
             "Sherlock Holmes and the Rune Stone Mystery: From the American Chronicles of John H. Watson M.D. (Sherlock Holmes)",["Larry Millett"],
             "The Jungle Book (Puffin Classics)",["Rudyard Kipling"], "Cosmic Connection:an Extraterrestrial Perspective",[ "Carl Sagan"],
             "Three wise men",["Martina Devlin"], "Healing and the Mind ",["Bill D. Moyers"],"No Way Out ",["Andrea Kane"], 
             "Night Of The Black Bird ",["Heather Graham"], "The Partner ",["John Grisham"], "Into the Inferno ",["EARL EMERSON"], 
             "In the Beauty of the Lilies ",["Chuck Palahniuk"],single_response=True)
    response("which book is trending?","which book is at no 1?","which book is trending nowadays", required_words=[""])
    response('You\'re welcome!', ['thank you. your site is sourceful!', 'thanks'], single_response=True)
    response('See you!', ['bye', 'goodbye', 'see you'], single_response=False)
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
