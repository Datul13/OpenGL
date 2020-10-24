from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def pikachu() :
    gluOrtho2D(-4.0, 4.0, -4.0, 4.0)
    glBegin(GL_LINES)
    glColor3f(1., 0., 1.)

    #1
    glVertex2f(-4.,3.25)
    glVertex2f(-2.,-0.25)

    #2
    glVertex2f(2.,-0.25)
    glVertex2f(4.,3.25)

    #3
    glVertex2f(0.65,0.5)
    glVertex2f(-0.65,0.5)

    #4
    glVertex2f(-2.,-0.25)
    glVertex2f(-2.,-1.75)

    #5
    glVertex2f(0.65,0.5)
    glVertex2f(4.,3.25)

    #6
    glVertex2f(-0.65,0.5)
    glVertex2f(-4.,3.25)

    #7
    glVertex2f(-2.,-1.75)
    glVertex2f(2.,-1.75)

    #8
    glVertex2f(2.,-1.75)
    glVertex2f(2.,-0.25)
    
    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Kelompok 3")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(pikachu)
glutMainLoop()
# End of program
