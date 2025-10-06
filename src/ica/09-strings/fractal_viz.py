"""
Visualizer for different fractals.

Sample fractals:
-  Prusinkiewicz1986: http://algorithmicbotany.org/papers/graphical-applications.pdf
-
"""

import turtle
from fractal.l_system import apply_l_system
from fractal.fractal_engine import draw_fractal


def draw_koch_curve(tur, n, angle, step_size):
    axiom = 'F'
    rules = {'F': 'F+F--F+F'}
    l_system = apply_l_system(axiom, rules, n)

    draw_fractal(tur, l_system, angle, step_size)


def draw_quadratic_koch_islad(tur, n, angle, step_size):
    axiom = 'F+F+F+F'
    rules = {'F': 'F+F-F-FF+F+F-F'}
    l_system = apply_l_system(axiom, rules, n)

    draw_fractal(tur, l_system, angle, step_size)


def draw_hilbert_curve(tur, n, angle, step_size):
    axiom = 'L'
    rules = {'L': '+RF-LFL-FR+', 'R': '-LF+RFR+FL-'}
    l_system = apply_l_system(axiom, rules, n)

    draw_fractal(tur, l_system, angle, step_size)


def draw_dragon_curve(tur, n, angle, step_size):
    axiom = 'F+F+F+F'
    rules = {'F': 'FF+F+F+F+FF'}
    l_system = apply_l_system(axiom, rules, n)

    draw_fractal(tur, l_system, angle, step_size)


def draw_combination_of_lacks_and_islands_curve(tur, n, angle, step_size):
    axiom = 'F+F+F+F'
    rules = {'F': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',
             'f': 'ffffff'}
    l_system = apply_l_system(axiom, rules, n)

    draw_fractal(tur, l_system, angle, step_size)

def draw_sierpinski_triangle(tur,n,step_size):
    axiom = 'FXF++FF++FF'
    rules = {'F':'FF',
            'X':'++FXF--FXF--FXF++'}
    l_system = apply_l_system(axiom,rules,n)
    draw_fractal(tur,l_system,60,step_size)

def draw_peano_gosper(tur,n,angle,step_size):
    axiom = 'FX'
    rules = {'X':'X+YF++YF-FX--FXFX-YF+',
             'Y':'-FX+YFYF++YF+FX--FX-Y'}
    l_system = apply_l_system(axiom,rules,n)
    draw_fractal(tur,l_system,angle,step_size)

if __name__ == '__main__':
    scr = turtle.Screen()
    tur = turtle.Turtle()
    tur.hideturtle()
    tur.speed(0)
    tur.up()
    tur.goto(-300,0)
    tur.down()

    draw_koch_curve(tur, 4, 30, 3) #angle = 60 is standard
    # draw_hilbert_curve(tur, 4, 90, 5)
    # draw_quadratic_koch_islad(tur, 3, 90, 5)
    # draw_dragon_curve(tur, 3, 90, 5)
    # draw_combination_of_lacks_and_islands_curve(tur, 2, 90, 5)
    # draw_sierpinski_triangle(tur,4,5)
    # draw_peano_gosper(tur,4,60,5)

    tur.up()
    tur.forward(50)
    tur.color('red')
    tur.write('done')
    scr.mainloop()
