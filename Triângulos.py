print('Para formar um Triangulo: ')
ladoA = int(input('Digite o tamanho do lado A: '))
ladoB = int(input('Digite o tamanho do lado B: '))
ladoC = int(input('Digite o tamanho do lado C: '))

def triangulo(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    return True
  else:
    return False

def tipo_triangulo(a, b, c):
  if a == b == c:
    return "equilátero"
  elif a == b or a == c or b == c:
    return "isósceles"
  else:
    return "escaleno"
