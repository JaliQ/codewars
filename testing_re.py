from random import randint
import re

name = "Bruce"
part = ["green", "black", "blue"]
x = randint(1, 5000)
tex = "Hola, %s! Your number is %-4d" % (name, x)
st = "welcomeToTheRe"
print(re.sub("([A-Z])", r" \1", st))
p = re.compile("[a-e]")
print(p.findall("Hey, I'm Josh!", 0, 12))
print(tex)
print(",".join(part[:-1]))
