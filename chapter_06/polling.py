favorite_languages = {
    'deus': 'python',
    'april': 'c++',
    'skyler': 'java',
    'devin': 'python',
}


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")    

coders = ['ryan', 'tom', 'deus', 'april', 'david', 'meriah', 'rose']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")