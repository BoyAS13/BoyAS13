text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."

inp1 = input()
inp2 = input()

def replacer():
    print(text.count(inp1))
    print(text.replace(inp1, inp2))

replacer()