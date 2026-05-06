#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Jordan Peetz

'''
This is a script an input and encode and decode BASE64
'''

#import libraries
import base64


def encode_to_base64(plaintext: str) -> str:
    '''
Encoding plain text to BASE64
Steps : 
1) convert string using UTF-8
2) Pass the bytes in to a function called b64.encode
3) Resulted bytes and return
    '''
    text_as_bytes = plaintext.encode("utf-8")
    encoded_bytes = base64.b64encode(text_as_bytes)
    return encoded_bytes.decode("utf-8")


def decode_to_base_64(encoded_text: str) -> str:
    '''
1) Taking base64 string back to original plaintext
2) Convert base84 string to get original bytes
3) Decode the byste back to utf-8 string
    '''
    encoded_as_bytes = encoded_text.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_as_bytes)
    return decoded_bytes.decode("utf-8")

#define main

def main():
    print("Base64 Encoder / Decoder")
    print("THIS IS NOT ENCRYPTION")
    #User input of what to encode
    message = input("Enter you message to encode: ").strip()
    #encode step
    if not message:
        print("Nothing Entered. Closing.")
        return
    #encode
    encoded = encode_to_base64(message)
    print(f"Base64 : {encoded}")

    #decode
    decoded = decode_to_base_64(encoded)

    #validation
    match = decoded == message
    print("Confirmed Match")
    print()



if __name__ == "__main__":
    main()