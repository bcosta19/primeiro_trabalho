import rpyc
import sys

if(len(sys.argv)) < 2:
    exit("Usage { } SERVER".format(sys.argv[0]))
    
server = sys.argv[1]
conn = rpyc.connect(server, 18861)

n = int(input("Digite o tamanho do vetor: "))

# Vetor de 1 a n - 1
vector = list(range(n))
print(f"Vetor gerado: {vector}")

soma = conn.root.sum_vector(vector)

print(f"A soma dos elementos do vetor é: {soma}")
conn.close()

