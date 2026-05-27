primeiro_termo = 1
segundo_termo = 1
fibonacci = []

for i in range(10):
    fibonacci.append(primeiro_termo)

    terceiro_termo = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo

print(fibonacci)
    