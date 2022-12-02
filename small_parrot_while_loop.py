prompt = "Tell me something and I will repeat it: \n"
prompt += "If you done click - quit"

message = ""
print(prompt)


while message != "quit":
    message = input()

    print(message)