curso01 = int(input("Digite a quantidade de acessos do curso01"))
curso02 = int(input("Digite a quantidade de acessos do curso02"))

if curso01 > curso02 :
    print("Curso01 tem mais acessos.")
elif curso01 < curso02 :
    print("Curso02 tem mais acessos.")
else:
    print("Ambos os cursos tiveram a mesma quantidade de acessos.")