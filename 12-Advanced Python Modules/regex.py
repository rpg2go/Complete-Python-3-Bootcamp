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

if __name__ == "__main__":
    #regex_basics()
    regex_syntax()
