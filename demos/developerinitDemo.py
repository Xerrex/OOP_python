from juice.Developer import Developer

'''
Demonstrates DRY __init__
'''

dev1 = Developer('AlexDev', 'Kagai', 50000, 'Java')
dev2 = Developer('Alex2Dev', 'Kagai2', 60000,'Python')

print(dev1.email)
print(dev1.prog_lang,"\n")

print("dev2 information in a dictionary")
print(dev2.__dict__)