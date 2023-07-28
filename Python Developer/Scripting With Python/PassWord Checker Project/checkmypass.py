import requests, hashlib, sys


def check_my_pass(query_char):

    hash_string_first_five,hash_string_tail = find_sha1_coding(query_char) # converting password we want to check into first 5 char of SHA1 code
    url = 'https://api.pwnedpasswords.com/range/' + hash_string_first_five
    response = requests.get(url)

    if response.status_code != 200:
         raise RuntimeError ('Please recheck yr API')
    
    result = grap_result(response, hash_string_tail)

    return result

 
def find_sha1_coding(str_obj):
    '''
    Converting str cobject into first 5 and remain char of its SHA1 hashed coding
    '''
    hash_object = hashlib.sha1(str_obj.encode('utf-8')).hexdigest().upper()
    return hash_object[:5], hash_object[5:]


def grap_result(response, hash_string_tail):
    index = response.text.find(hash_string_tail)
        
    if index == -1:
        return 0
    else:
        return extract_int_until_non_int(response.text[index+36:])



# predefined function by help of ChatGPT to get int value out of set of text '54852 D090CA3' ==> '54852'
def extract_int_until_non_int(input_string):
    num_str = ""
    for char in input_string:
        if char.isdigit():
            num_str += char
        else:
            break
    if num_str:
        return int(num_str)
    else:
        return None


def main():
    my_pass_list = sys.argv[1:]
    for my_pass in my_pass_list:
        print(f"the pass {my_pass}, have been reached {check_my_pass(my_pass)} times")

if __name__ == '__main__':
    sys.exit(main())
    
#print(sys.argv[0])
