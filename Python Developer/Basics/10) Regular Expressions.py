import re
# https://regex101.com/

string = 'hello my name is my my'
text = r"([a-z]).([l])"

search = re.search('hello', string)
#print(search.span())
#print(search.start())
#print(search.end())
#print(search.group())


# using pattern on searching

pattern = re.compile(text)

print(pattern.search(string).group())
print(pattern.findall(string))
print(pattern.match(string))
print(pattern.fullmatch(string))

# by help of ChatGPT below function used to validate entered emails

def is_valid_email(email):
    # Regular expression pattern for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Example usage:
customer_email = 'hamzatarq98@gmail.com'
if is_valid_email(customer_email):
    print("Valid email!")
else:
    print("Invalid email!")