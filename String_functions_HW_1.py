import string

def count_characters(input_string):
    num_count = sum(1 for char in input_string if char.isdigit())
    lower_count = sum(1 for char in input_string if char.islower())
    upper_count = sum(1 for char in input_string if char.isupper())
    symbol_count = sum(1 for char in input_string if char in string.punctuation)

    print("Number of numeric characters:", num_count)
    print("Number of lowercase characters:", lower_count)
    print("Number of uppercase characters:", upper_count)
    print("Number of symbols:", symbol_count)



# Test count_characters function
input_string = '''n<V}wePdAA`9kE2?
u@jmzB="nMLLH6Ee
K}s?3UdG_t:m=+Wz
N7pKt`N/Y2Pcr/mS
K^5Vk&EA!?`6aB@$'''
print(" Individual Character counts:")
count_characters(input_string)
print()




