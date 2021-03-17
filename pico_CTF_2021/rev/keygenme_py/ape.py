hash = "92d7ac3c9a0cf9d527a5906540d6c59c80bf8d7ad5bb1885f5f79b5b24a6d387"
loc = [4, 5, 3, 6, 2, 7, 1, 8]
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
print(key_part_static1_trial, end='')
for i in loc:
    print(hash[i], end='')

print(key_part_static2_trial, end='')
