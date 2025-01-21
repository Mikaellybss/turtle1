import turtle

esguicho = turtle.Turtle()


def desenhe_uma_flor():
 for i in range(12):
  esguicho.forward(60)
  esguicho.left(30)
  esguicho.forward(60)
  esguicho.left(150)
  esguicho.forward(60)
  esguicho.left(30)
  esguicho.forward(60)


def andar (pixels):
    esguicho.penup()
    esguicho.forward(pixels)
    esguicho.pendown()



desenhe_uma_flor()
andar(250)
desenhe_uma_flor()
