prompt = "\nI am a parrot. Say something and I will repeat it"
prompt += '\nIf you want to exit, print "Exit"  '

active = True

while active:
    message = input(prompt)

    if message == 'Exit':
        active = False
    else:
        print(message)
