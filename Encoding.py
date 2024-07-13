letters = 'abcdefghijklmnopqrstuvwxyz'


def encoding_function(message, shift):
    for i in range(len(message)):
        inx = letters.find(message[i])
        message = list(message)
        final_inx = inx + shift

        # let's say we have in the message the letter (  z  ) , and we want to shift it 2 times,
        # it's going to be out of range since z is the last letter, so what we do is ->
        # keeping ( final_inx ) in the range of 25 or ( len(letters) - 1 )
        if message[i] in letters:
            if inx + shift > len(letters) - 1:
                final_inx = (inx + shift - 1) - (len(letters) - 1)
                message[i] = letters[final_inx]
            else:
                message[i] = letters[final_inx]
        else:
            message[i] = message[i]

    message = "".join(message)
    return message
