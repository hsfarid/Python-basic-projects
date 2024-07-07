message = input("> ")

def emoji_convertor(message):
    words = message.split(" ")

    emoji_mapping = {
    ":)":"😊",
    ":(":"😢"
    }

    output =""
    for word in words:
        output += emoji_mapping.get(word, word) + " "
    return output

    
print(emoji_convertor(message))

