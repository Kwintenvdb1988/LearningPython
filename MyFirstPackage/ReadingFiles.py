from sys import argv

script, fileName = argv

txt = open(fileName, 'r')

print(txt.read())
#txt.writable()
#txt.write('hello to you too')
txt.close()

