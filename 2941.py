sentence = input()

special = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in special:
    sentence = sentence.replace(alphabet, "a")
    
print(len(sentence))