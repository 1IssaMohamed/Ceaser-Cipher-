def engima_light():
    #create key strings (for encryption)
    keys=("abcdefghijklmnopqrstuvwxyz !")
    #autogen the value string by ofsettign original string
    values = keys[-1]+keys[0:-1] #moves last char to first, first char to last
    print(keys,values)
    #creating 2 dictionaries (1 for encodign and antoher decoding)
    dict_e=dict(zip(keys,values))
    print(dict_e)
    dict_d=dict(zip(values,keys))
    #user input the message adn mdoe (encrypt/decrypt)
    message=input("Enter your crypto message:")
    mode=input("Crypto Mode?\na)Encode(e)\nb)Decrypt(d)")
    #run encode or decode
    # while mode!='e' or mode!='a':
    valid=False
    while not valid:
        if mode=='e':
            new_msg=''.join([dict_e[x] for x in message])
            valid=True
        elif mode=='d':
            new_msg=''.join([dict_e[x] for x in message])
            valid=True
        else:
            mode=input("Invalid entry, retry?\na)Encode(e)\nb)Decrypt(d)")

    #return results
    return new_msg
    #clean and beautify the code
print(f"new message:{engima_light()}")