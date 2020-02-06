d = {}
# or d = dict{}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16
print(d["George"])
d[10] = 100
print(d)

# how to iterate over key value pairs
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print(" ")
