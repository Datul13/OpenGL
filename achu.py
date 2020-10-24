from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def pikachu() :
    gluOrtho2D(-6.0, 6.0, -9.0, 5.0)
    glBegin(GL_LINES)

    #1
    glColor3f(0., 0., 0.)
    glVertex2f(-4.,4.25)
    glVertex2f(-2.,0.75)

    #2
    glColor3f(0., 0., 0.)
    glVertex2f(2.,0.75)
    glVertex2f(4.,4.25)

    #3
    glColor3f(1., 1., 0.)
    glVertex2f(0.65,1.5)
    glVertex2f(-0.65,1.5)

    #4
    glColor3f(1., 1., 0.)
    glVertex2f(-0.65,1.5)
    glVertex2f(-2.0,0.75)

    #5
    glColor3f(1., 1., 0.)
    glVertex2f(-2.,0.75)
    glVertex2f(-2.,-1.75)

    #6
    glColor3f(1., 1., 0.)
    glVertex2f(0.65,1.5)
    glVertex2f(2.0,0.75)
    

    #7
    glColor3f(0., 0., 0.)
    glVertex2f(0.65,1.5)
    glVertex2f(4.,4.25)

    #8
    glColor3f(0., 0., 0.)
    glVertex2f(-0.65,1.5)
    glVertex2f(-4.,4.25)

    #9
    glColor3f(1., 1., 0.)
    glVertex2f(-2.,-1.75)
    glVertex2f(2.,-1.75)

    #10
    glColor3f(1., 1., 0.)
    glVertex2f(2.,0.75)
    glVertex2f(2.,-1.75)

    glEnd()

    glBegin(GL_POLYGON)

    glColor3f(0., 0., 0.)
    glVertex2f(-4.,-2.)
    glVertex2f(-0.65,-4.75)
    glVertex2f(-2.,-5.5)

    glEnd()

    glBegin(GL_POLYGON)

    glColor3f(1., 1., 0.)
    glVertex2f(-0.65,-4.75)
    glVertex2f(-2.,-5.5)
    glVertex2f(0.,-5.5)

    glVertex2f(0.,-5.5)
    glVertex2f(-0.65,-4.75)
    glVertex2f(0.65,-4.75)
    
    glVertex2f(2,-4.75)
    glVertex2f(2.,-5.5)
    glVertex2f(2.,-5.5)

    glVertex2f(0.,-5.5)
    glVertex2f(-2.,-5.5)
    glVertex2f(-2.,-6.63)

    glVertex2f(-2.,-6.63)
    glVertex2f(0.,-5.5)
    glVertex2f(2.,-8.)

    glVertex2f(-2.,-6.63)
    glVertex2f(2.,-5.5)
    glVertex2f(2.,-8.0)

    glVertex2f(0.,-8.0)
    glVertex2f(-2.,-8.0)
    glVertex2f(-2.,-6.63)

    glEnd()

    glBegin(GL_POLYGON)

    glColor3f(0., 0., 0.)
    glVertex2f(4.,-2.)
    glVertex2f(2.,-5.5)
    glVertex2f(0.65,-4.75)

    glEnd()
    
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Kelompok 3")
glClearColor(1.0, 1.0, 1.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT)
glutDisplayFunc(pikachu)
glutMainLoop()
# End of program
