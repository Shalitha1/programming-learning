
class StringReverser:

    def reverser(self, text):
        reversed_text = ""

        for i in text:
            reversed_text = i + reversed_text

        return reversed_text

obj = StringReverser()
result = obj.reverser("Hutto")

print(result)