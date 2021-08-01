# ERRADO USA MUIOTA MEMORIA
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=" ")
print("Acabou")

# CORRETO USA MENAS MEMORIA
for c in range(2, 51, 2):
    if c % 2 == 0:
        print(c, end=" ")
print("Acabou")
