encoded_string = raw_input("Enter the hex encoded string\n")
converted = encoded_string.decode("hex").encode("base64")
print converted
