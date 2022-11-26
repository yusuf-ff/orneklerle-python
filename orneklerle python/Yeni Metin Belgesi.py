
import turtle
# Turtle kütüphanesinden bir nesne oluşturuyoruz.
ucgen = turtle.Turtle()
# Kalem nesnesine renk veriyoruz
ucgen.pencolor("red")
#Kalem nesnesine kalınlık veriyoruz.
ucgen.pensize(2)
# Kalem nesnesine çizim hızı veriyoruz
ucgen.speed(7)
# Döngü ile çizgi uzunluğu ve açısına göre çizim yaptırıyoruz.
for i in range(41):
    ucgen.forward(300)
    ucgen.right(123)
turtle.done()
 