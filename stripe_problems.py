# Given a String, split it into major parts separated by special char '/'. For each major part that’s split by '/', we can further split it into minor parts separated by '.'.

# ### Example 1
# str = stripe.com/payments/checkout/customer.john.doe
# minor_parts = 2
# after Part 1 compression
# =>
# s4e.c1m/p6s/c6t/c6r.j2n.d1e
# after Part 2 compression
# =>
# s4e.c1m/p6s/c6t/c6r.j5e

# ### Example 2
# Given:
# str = www.api.stripe.com/checkout
# minor_parts = 3
# (after Part 1 compression)
# =>
# w1w.a1i.s4e.c1m/c6t
# (then after Part 2 compression)
# =>
# w1w.a1i.s7m/c6t

class StripeCompression():
    def __init__(self, input: str, minor_parts: int, major_delim :str = "/" , minor_delim :str = "."):
        self.input = input
        self.major_delim = major_delim
        self.minor_delim = minor_delim
        self.minor_parts = minor_parts

    def compress_word(self, word):
        if len(word) <=2:
            return word
        return word[0]+str(len(word)-2)+word[-1]
    
    def compress_minor_word(self, word):
        if self.minor_delim in word:
            word = word.replace(self.minor_delim, "")
        if len(word) <=2:
            return word
        return word[0]+str(len(word)-2)+word[-1]
    
    def compress_string(self):
        res=[]
        # split by major delimiter:
        for word in self.input.split(self.major_delim):
            if self.minor_delim in word:
                word_compressed = []
                for minor_word in word.split(self.minor_delim, maxsplit=self.minor_parts-1):
                    word_compressed.append(self.compress_minor_word(minor_word))
                res.append(".".join(word for word in word_compressed))
            else:
                res.append(self.compress_word(word))
        return "/".join(word for word in res)
    
# Home Work:

# Given an inputString(s) input source and target source, return the shipping price to send packages from one county to the next.
# ex:
# input = "US:UK:Fedex:5, CA:FR:DHL:10, FR:UK:UPS:6"
# function costOfPackages(input, "US", "UK) -> 5
# function costOfPackages(input, "FR", "UK) -> 6

# Follow up Question: If given the input string, starting destination and ending destination, calculate the total shipping cost from the starting country to the ending

# input = "US:UK:Fedex:5, CA:FR:DHL:10, FR:UK:UPS:6, UK:US:DHL:2, UK:FR:DHL:10"
# function costOfPackages(input, "US", "FR") -> US to UK then UK to FR -> 15





if __name__ == '__main__':
    compressor = StripeCompression(input="stripe.com/payments/checkout/customer.john.doe", minor_parts=2)
    print(compressor.compress_string())
    compressor = StripeCompression(input="www.api.stripe.com/checkout", minor_parts=3)
    print(compressor.compress_string())

        

