coordenadaX = int(input("Didite a coordenada X: "))
coordenadaY = int(input("Didite a coordenada Y: "))

if coordenadaX > 0 and coordenadaY > 0:
    print("As coordenadas estão no primeiro quandrante")
elif coordenadaX <0 and coordenadaY > 0:
    print("As coordenadas estão no segundo quadrante")
elif coordenadaX < 0 and coordenadaY < 0:
    print("As coordenas estão no terceiro quadrante")
elif coordenadaX > 0 and coordenadaY > 0:
    print("As coordenadas estão no quarto quadrante")
else:
    print("O ponto está no eixo de origem")

