import string

mussum_ipsum = 'Mussum Ipsum, cacilds vidis litro abertis. Praesent malesuada urna nisi, quis volutpat erat hendrerit non. Nam vulputate dapibus. Sapien in monti palavris qui num significa nadis i pareci latim. Si u mundo tá muito paradis? Toma um mé que o mundo vai girarzis! Atirei o pau no gatis, per gatis num morreus.'

ipsum_list = mussum_ipsum.split(' ')

from ipdb import set_trace; set_trace()

list_sixth_letter = []
for word in ipsum_list:
    try:
        char = word[5]
        if char in string.ascii_letters:
            list_sixth_letter.append(word[5])
    except IndexError:
        pass

print(list_sixth_letter)