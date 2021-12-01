w=input('ENTER A WORD:')
for ch in w:
    if ch in'aeiouAEIOU':
        print('GIVEN WORD CONTAINS VOWELS')
        break
else:
    print('GIVEN WORD DOES NOT CONTAINS ANY VOWELS')