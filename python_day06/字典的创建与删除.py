d = {10: "dog", 20: "cat", 30: "pet", 20: "zool"}
print(d)

list1 = [10, 20, 30]
list2 = ["apple", "banala", "orange", "peer"]
zipobj = zip(list1, list2)
num = dict(zipobj)
print(num)

t = (10, 20, 30)

print({t: "dog"})
print({t: 10})
