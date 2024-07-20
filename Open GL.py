import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*
vertex = ((1,1,-1),(-1,1,-1),(1,-1,-1),(-1,-1,1),(1,1,1),(1,-1,1),(-1,1,1),(-1,-1,-1))
edges = ((0,1),(0,2),(0,4),(2,7),(2,5),(3,7),(6,3),(6,4),(6,1),(5,4),(5,3),(7,1))
def verticies():
    glBegin(GL_LINES)
    for h in edges:
        for i in h:
            glVertex3fv(vertex[i])
    glEnd() 

def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode (display,DOUBLEBUF|OPENGL)
    gluPerspective(50,(display[0]/display[1]),1,50)
    glTranslatef (0.0,0,-9)
    glRotatef(0,0,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
        glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        verticies()
        glRotatef(1,1,1,1)
        pygame.display.flip()
        pygame.time.wait(10)
main()
