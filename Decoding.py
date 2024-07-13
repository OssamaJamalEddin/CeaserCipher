letters = 'abcdefghijklmnopqrstuvwxyz'


def decoding_function(message, shift):
    for i in range(len(message)):
        inx = letters.find(message[i])
        message = list(message)
        final_inx = inx - shift
        # We do here as we did in Encoding but vice versa since we are going backwards not forward
        if message[i] in letters:
            if inx - shift < 0:
                final_inx = (inx - shift + 1) + (len(letters) - 1)
                message[i] = letters[final_inx]
            else:
                message[i] = letters[final_inx]
        else:
            message[i] = message[i]
    message = "".join(message)
    return message
