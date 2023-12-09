import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.raw.GLU import gluOrtho2D

from engine.camera import Camera
from engine.scene.scene_manager import SceneManager
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Key, Keys


class PicoCore:
    __KEY_STATES = {}
    __MOUSE_CLICK_POSITION = (0, 0)
    __scene_manager = SceneManager()

    @staticmethod
    def is_pressed(key: Key, hold=True):
        if hold:
            return PicoCore.__KEY_STATES.get(key.value, False)
        else:
            if PicoCore.__KEY_STATES.get(key.value, False):
                PicoCore.__KEY_STATES[key.value] = False
                return True
            else:
                return False

    @staticmethod
    def get_click_position():
        return PicoCore.__MOUSE_CLICK_POSITION

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_objects = []
        self.last_frame_time = time.time()
        position = [0.0, 0.0]  # Set the camera's initial position (x, y)
        zoom = 1.0  # Set the initial zoom level
        self.camera = Camera(position, zoom)
        self.game_over = False

    @staticmethod
    def get_scene_manager() -> SceneManager:
        return PicoCore.__scene_manager

    def add_game_object(self, game_object: GameObject):
        self.game_objects.append(game_object)

    def remove_game_object(self, game_object: GameObject):
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)

    def __display(self):

        def draw_recursive(game_object):
            glPushMatrix()
            glTranslatef(game_object.x, game_object.y, 0)
            glRotatef(game_object.rotation, 0, 0, 1)
            glScalef(game_object.scale, game_object.scale, 1)
            game_object.draw()

            for child in game_object.children:
                draw_recursive(child)

            glPopMatrix()

        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        scene = PicoCore.get_scene_manager().get_current_scene()

        for ui_object in scene.ui_objects:
            draw_recursive(ui_object)

        glScalef(scene.camera.zoom, scene.camera.zoom, 1)
        glTranslatef(-scene.camera.position[0], -scene.camera.position[1], 0)

        for game_object in scene.game_objects:
            draw_recursive(game_object)

        if self.game_over:
            # Display "Game Over" message
            Draw.change_color("#FF0000")
            Draw.text("GAME OVER", self.width // 2 - 135, self.height // 2, size=30)

        glutSwapBuffers()

    def __update(self, value):
        if not self.game_over:
            current_frame_time = time.time()
            delta_time = (current_frame_time - self.last_frame_time) * 1000  # Convert to milliseconds
            self.last_frame_time = current_frame_time

            scene = PicoCore.get_scene_manager().get_current_scene()
            scene.camera.update(delta_time)

            def update_recursive(game_object: GameObject):
                if not game_object.started:
                    game_object.start()
                    game_object.started = True
                game_object.update(delta_time)

                for child in game_object.children:
                    update_recursive(child)

            for ui_object in scene.ui_objects:
                update_recursive(ui_object)

            for ui_object in scene.ui_objects:
                if ui_object.to_remove:
                    scene.remove_game_object(ui_object)

            if not scene.paused:
                for game_object in scene.game_objects:
                    update_recursive(game_object)

                for game_object in scene.game_objects:
                    if game_object.to_remove:
                        scene.remove_game_object(game_object)

        glutPostRedisplay()
        glutTimerFunc(16, self.__update, 0)

    def exit(self):
        glutLeaveMainLoop()

    def __keyboard(self, key, x, y):
        if not PicoCore.__KEY_STATES.get(key):
            PicoCore.__KEY_STATES[key] = True

    def __keyboard_up(self, key, x, y):
        PicoCore.__KEY_STATES[key] = False

    def __mouse(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            PicoCore.__KEY_STATES[Keys.LMB.value] = state == GLUT_DOWN
        elif button == GLUT_RIGHT_BUTTON:
            PicoCore.__KEY_STATES[Keys.RMB.value] = state == GLUT_DOWN
        PicoCore.__MOUSE_CLICK_POSITION = (x, self.height - y)

    def run(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_MULTISAMPLE)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(bytes(self.title, "utf-8"))

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        gluOrtho2D(0.0, self.width, 0.0, self.height)
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glutTimerFunc(16, self.__update, 0)
        glutDisplayFunc(self.__display)
        glutSpecialFunc(self.__keyboard)
        glutSpecialUpFunc(self.__keyboard_up)
        glutKeyboardFunc(self.__keyboard)
        glutKeyboardUpFunc(self.__keyboard_up)
        glutMouseFunc(self.__mouse)
        glutMainLoop()
