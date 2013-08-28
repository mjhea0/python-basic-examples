#coding:utf-8

#manual
f = open('/etc/motd', 'r')

longest = 0
allLines = f.readlines()
f.close()

for line in allLines:
    linelen = len(line.strip())
    if linelen > longest:
        longest = linelen

print longest

#buildin max function
f = open('/etc/motd', 'r')
allLineLens = [len(x.strip()) for x in f]
f.close()

print max(allLineLens)
