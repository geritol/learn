# simple viginere cipher, where the key is repeated
class VigenereCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc

    def code(self, text, way = 'en'):
        res = ''
        count = 0
        for char in text:
            if char not in self.abc:
                res += char
            else:
                curr = self.abc.index(char)
                shift = self.abc.index(self.key[count % len(self.key)])
                if way == 'de': shift = -shift
                res += self.abc[(curr + shift) % len(self.abc)]
                count += 1
        return ''.join(res)

    def encode(self, text):
        return self.code(text, 'en')

    def decode(self, text):
        return self.code(text, 'de')


# here the key is only used once, and then replaced by the decoded text.
class VigenereAutokeyCipher(VigenereCipher):

    def code(self, text, way='en'):
        count = 0
        key = self.key
        res = ''
        for char in text:
            if char not in self.abc:
                res += char
            else:
                curr = self.abc.index(char)
                shift = self.abc.index(key[count])
                if way == 'de':
                    res = res + self.abc[(curr - shift) % len(self.abc)]
                    key += res[-1]
                else:
                    res = res + self.abc[(curr + shift) % len(self.abc)]
                    key += char
                count += 1
        return res


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'PASSWORD'

c = VigenereCipher(key, alphabet)
ca = VigenereAutokeyCipher(key, alphabet)

assert c.encode('AAAAAAAA PASSWORD AAAAAAAA') == c.encode(c.decode('PASSWORD EAKKSCIG PASSWORD'))

assert ca.encode('AAAAAAAA PASSWORD AAAAAAAA') == ca.encode(ca.decode('PASSWORD PASSWORD PASSWORD'))
