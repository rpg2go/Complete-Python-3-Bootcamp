import re

def regex_basics():
    text = "The person's phone number is 408-555-1234. Call soon!"
    pattern = 'phone'

    # simple match
    print(re.search(pattern,text))
    match = re.search(pattern,text)
    print(match.start())
    print(match.end())

    # multiple matches
    text = "my phone is a new phone"
    match = re.search("phone", text)
    print(match)

    matches = re.findall("phone", text)
    print(matches)
    print(len(matches))

    for match in re.findall("phone", text):
        print(match)

    for match in re.finditer("phone", text):
        print(match)

    for match in re.finditer("phone", text):
        print(match.span(), " - ", match.group())


def regex_syntax():
    text = "My telephone number is 408-555-1234"

    phone = re.search("408-555-7777", text)
    print(phone)

    phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
    print(phone)

    phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
    print(phone)

    phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    results = re.search(phone_pattern, text)
    print(results.group())
    print(results.group(1), results.group(2), results.group(3))

def regex_part3():

    # or operator
    result = re.search(r'cat|dog', 'The cat & dogs are here')
    print(result)

    #find all
    result = re.findall(r'...at', 'The cat in the hat went splat')
    print(result)

    # start with
    result = re.findall(r'^\d', '6 cats are here')
    print(result)

    # end with
    result = re.findall(r'\d$', 'The number is two 2')
    print(result)

    # exclude patterns
    pattern = r'[^\d]+'
    result = re.findall(pattern, 'There are 3 numbers 34 inside 5 this sentence')
    print(result)

    # remove simbols
    result = re.findall(r'[^!.?]+', 'This is a string! But is has punction. How can we remote it')
    print(result)
    print(''.join(result))

    # include patterns
    pattern = r'[^\d]+'
    result = re.findall(pattern, 'There are 3 numbers 34 inside 5 this sentence')
    print(result)

    # Brackets for Grouping
    text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
    pattern = r'[\w]+-[\w]+'
    result = re.findall(pattern, text)
    print(result)

    # Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
    text = 'Hello, would you like some catfish?'
    texttwo = "Hello, would you like to take a catnap?"
    textthree = "Hello, have you seen this caterpillar?"

    pattern = r'cat(fish|nap|claw)'
    print(re.findall(pattern, text))
    print(re.findall(pattern, texttwo))
    print(re.findall(pattern, textthree))

if __name__ == "__main__":
    #regex_basics()
    #regex_syntax()
    regex_part3()

