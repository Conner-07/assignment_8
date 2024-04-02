
import string

def decode_acrostic(acrostic, starting_line=0):
    secret_message = ''.join(line[starting_line] for line in acrostic.split("\n") if line)
    return secret_message

# Testing the function
acrostic = '''SATOR\n
AREPO\n
TENET\n
OPERA\n
ROTAS\n'''

secret_message = decode_acrostic(acrostic)
print("Decoded secret message:", secret_message)



