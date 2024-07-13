import Encoding
import Decoding


running = 'YES'
while running == 'YES':
    decision = input("Would you like to decode or encode ? \nEnter: ").upper()
    message = input("Enter the message: ")
    shifting = int(input("Enter the shifting number: "))
    output = ""
    if decision == "ENCODE":
        output = Encoding.encoding_function(message, shifting)
    elif decision == "DECODE":
        output = Decoding.decoding_function(message, shifting)
    else:
        # raise Exception("Type error occurred, make sure to write (Encode/Decode) correctly")
        print("Make sure you wrote Encode/Decode correctly.")
        break
    print(output)
    running = input("Want to encode/decode more ? (Yes / No): ").upper()
