import math
#from math import radians, cos, sin, tan
valor = float(input('digite um valor'))

sen = math.sin(math.radians(valor))
cos = math.cos(math.radians(valor))
tan = math.tan(math.radians(valor))

print('o valor em radianos é {}\n'
      'o valor em seno é {:.2f}\n'
      'o valor em cosseno é {:.2f}\n'
      'o valor em tangente é {:.2f}\n'
      .format(math.radians(valor),
              sen, cos, tan))