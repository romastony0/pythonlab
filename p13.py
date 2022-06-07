import re;

s = """ hi vishwanath4vishwa@gmail.com and vvenkat@gmail.com""";

reg = re.findall('\S+@\S+',s);
print(reg)