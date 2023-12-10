from OpenGL.GL import *


class Draw:
    @staticmethod
    def point(x, y, size=1):
        glPointSize(size)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    @staticmethod
    def __find_zone(x1, y1, x2, y2):

        dx = x2 - x1
        dy = y2 - y1

        if dx >= 0 and dy >= 0:
            if abs(dx) >= abs(dy):
                return 0
            else:
                return 1
        if dx <= 0 and dy >= 0:
            if abs(dx) >= abs(dy):
                return 3
            else:
                return 2
        if dx <= 0 and dy <= 0:
            if abs(dx) >= abs(dy):
                return 4
            else:
                return 5
        if dx >= 0 and dy <= 0:
            if abs(dx) >= abs(dy):
                return 7
            else:
                return 6

    @staticmethod
    def __to_zone0(x1, y1, x2, y2, zone):
        if zone == 0:
            return x1, y1, x2, y2
        elif zone == 1:
            return y1, x1, y2, x2
        elif zone == 2:
            return y1, -x1, y2, -x2
        elif zone == 3:
            return -x1, y1, -x2, y2
        elif zone == 4:
            return -x1, -y1, -x2, -y2
        elif zone == 5:
            return -y1, -x1, -y2, -x2
        elif zone == 6:
            return -y1, x1, -y2, x2
        elif zone == 7:
            return x1, -y1, x2, -y2
        return x1, y1, x2, y2

    @staticmethod
    def __to_zone(x, y, zone):
        if zone == 0:
            return x, y
        if zone == 1:
            return y, x
        if zone == 2:
            return -y, x
        if zone == 3:
            return -x, y
        if zone == 4:
            return -x, -y
        if zone == 5:
            return -y, -x
        if zone == 6:
            return y, -x
        if zone == 7:
            return x, -y

    @staticmethod
    def line(x1, y1, x2, y2, width=2):
        zone = Draw.__find_zone(x1, y1, x2, y2)
        x1, y1, x2, y2 = Draw.__to_zone0(x1, y1, x2, y2, zone)

        dx = x2 - x1
        dy = y2 - y1

        d = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)
        y = int(y1)

        for x in range(int(x1), int(x2) + 1):
            p_x, p_y = Draw.__to_zone(x, y, zone)
            Draw.point(p_x, p_y, width)
            if d > 0:
                d = d + incNE
                y = y + 1
            else:
                d = d + incE

    @staticmethod
    def circle(r, cx, cy, fill=False, thickness=1):
        d = 1 - r
        x = 0
        y = r

        while x < y:
            if d < 0:
                d = d + (2 * x) + 3
                x += 1
            else:
                d = d + (2 * x) - (2 * y) + 5
                x += 1
                y -= 1

            if not fill:
                Draw.point(cx + y + r, cy + x + r, thickness)  # Zone 0
                Draw.point(cx + x + r, cy + y + r, thickness)  # Zone 1
                Draw.point(cx - x + r, cy + y + r, thickness)  # Zone 2
                Draw.point(cx - y + r, cy + x + r, thickness)  # Zone 3
                Draw.point(cx - y + r, cy - x + r, thickness)  # Zone 4
                Draw.point(cx - x + r, cy - y + r, thickness)  # Zone 5
                Draw.point(cx + x + r, cy - y + r, thickness)  # Zone 6
                Draw.point(cx + y + r, cy - x + r, thickness)  # Zone 7
            else:
                Draw.line(cx - x + r, cy + y + r, cx + x + r, cy + y + r)  # Zone 1 and 2
                Draw.line(cx - y + r, cy + x + r, cx + y + r, cy + x + r)  # Zone 0 and 3
                Draw.line(cx - y + r, cy - x + r, cx + y + r, cy - x + r)  # Zone 4 and 7
                Draw.line(cx - x + r, cy - y + r, cx + x + r, cy - y + r)  # Zone 5 and 6

                Draw.line(cx + y + r, cy - x + r, cx + y + r, cy + x + r)  # Zones 0 and 7
                Draw.line(cx + x + r, cy - y + r, cx + x + r, cy + y + r)  # Zones 1 and 6
                Draw.line(cx - x + r, cy - y + r, cx - x + r, cy + y + r)  # Zones 2 and 5
                Draw.line(cx - y + r, cy - x + r, cx - y + r, cy + x + r)  # Zones 3 and 4

    @staticmethod
    def rect(x, y, width, height, fill=False):
        Draw.line(x, y, x + width, y)
        Draw.line(x, y, x, y - height)
        Draw.line(x, y - height, x + width, y - height)
        Draw.line(x + width, y, x + width, y - height)

        if fill:
            for i in range(height):
                Draw.line(x, y - i, x + width, y - i)
            for i in range(width):
                Draw.line(x + i, y, x + i, y - height)

    @staticmethod
    def change_color(color: str):
        rgb = Draw.hex_to_rgb_normalized(color)
        glColor3f(rgb[0], rgb[1], rgb[2])

    @staticmethod
    def rgba_to_hex(color):
        r, g, b = color
        return f"#{r:02x}{g:02x}{b:02x}"

    @staticmethod
    def hex_to_rgb_normalized(hex_color):
        if hex_color.startswith('#') and len(hex_color) == 7:
            hex_color = hex_color[1:]
        else:
            msg = f"Not a valid hex color {hex_color}"
            raise TypeError(msg)

        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)

        return r / 255.0, g / 255.0, b / 255.0

    @staticmethod
    def text(text, x, y, size=10, spacing=5):

        for char in text:
            Draw._draw_char(char, int(x), int(y), size)
            x += size + spacing

    @staticmethod
    def _draw_char(char, x, y, size):
        half_size = size / 2
        if char == 'A':
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - size / 2, x + size, y - size / 2)  # middle
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
        elif char == 'B':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + size / 2, y)  # top_left
            Draw.line(x, y - size / 2, x + size / 2, y - size / 2)  # middle_left
            Draw.line(x, y - size, x + size / 2, y - size)  # bottom_left
            Draw.line(x + size / 2, y, x + size / 2, y - size / 2)  # top_right
            Draw.line(x + size / 2, y - size / 2, x + size / 2, y - size)  # bottom_right
        elif char == 'C':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == 'D':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + half_size, y)  # top_left
            Draw.line(x, y - size, x + half_size, y - size)  # bottom_left
            Draw.line(x + half_size, y, x + half_size, y - size)  # right
        elif char == 'E':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - half_size, x + size, y - half_size)  # middle
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == 'F':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - half_size, x + size, y - half_size)  # middle
        elif char == 'G':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - size, x + size, y - size)  # bottom
            Draw.line(x + size, y - size, x + size, y - half_size)  # right_bottom
            Draw.line(x + half_size, y - half_size, x + size, y - half_size)  # middle_right
        elif char == 'H':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y - half_size, x + size, y - half_size)  # middle
        elif char == 'I':
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x + half_size, y, x + half_size, y - size)  # middle
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == 'J':
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y - size, x + size, y - size)  # bottom
            Draw.line(x + half_size, y, x + half_size, y - half_size)  # top_right
        elif char == 'K':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y - half_size, x + size, y)  # top_right
            Draw.line(x, y - half_size, x + size, y - size)  # bottom_right
        elif char == 'L':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == 'M':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y, x + half_size, y - half_size)  # middle_left
            Draw.line(x + size, y, x + half_size, y - half_size)  # middle_right
        elif char == 'N':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y, x + size, y - size)  # diagonal
        elif char == 'O':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == 'P':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - half_size, x + size, y - half_size)  # middle
            Draw.line(x + size, y, x + size, y - half_size)  # right_top
        elif char == 'Q':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - size, x + size, y - size)  # bottom
            Draw.line(x + half_size, y - half_size, x + size, y - size)  # diagonal
        elif char == 'R':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y - half_size, x + size, y - half_size)  # middle
            Draw.line(x + size, y, x + size, y - half_size)  # right_top
            Draw.line(x, y - half_size, x + size, y - size)  # diagonal_bottom_right
        elif char == 'S':
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x, y, x, y - half_size)  # left_top
            Draw.line(x, y - half_size, x + size, y - half_size)  # middle
            Draw.line(x + size, y - half_size, x + size, y - size)  # right_bottom
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == 'T':
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x + half_size, y, x + half_size, y - size)  # middle
        elif char == 'U':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == 'V':
            Draw.line(x, y, x + half_size, y - size)  # left_diagonal
            Draw.line(x + size, y, x + half_size, y - size)  # right_diagonal
        elif char == 'W':
            Draw.line(x, y, x, y - size)  # left
            Draw.line(x + size, y, x + size, y - size)  # right
            Draw.line(x, y - size, x + half_size, y - half_size)  # bottom_left_diagonal
            Draw.line(x + size, y - size, x + half_size, y - half_size)  # bottom_right_diagonal
        elif char == 'X':
            Draw.line(x, y, x + size, y - size)  # left_diagonal
            Draw.line(x + size, y, x, y - size)  # right_diagonal
        elif char == 'Y':
            Draw.line(x, y, x + half_size, y - half_size)  # left_top_diagonal
            Draw.line(x + size, y, x + half_size, y - half_size)  # right_top_diagonal
            Draw.line(x + half_size, y - half_size, x + half_size, y - size)  # middle
        elif char == 'Z':
            Draw.line(x, y, x + size, y)  # top
            Draw.line(x + size, y, x, y - size)  # diagonal
            Draw.line(x, y - size, x + size, y - size)  # bottom
        elif char == '.':
            Draw.line(x + half_size / 2, y - size, x + half_size / 2, y - size)
        elif char.isdigit() and 0 <= int(char) <= 9:
            if char == '0':
                Draw.line(x, y, x, y - size)
                Draw.line(x, y, x + size, y)
                Draw.line(x + size, y, x + size, y - size)
                Draw.line(x, y - size, x + size, y - size)
            elif char == '1':
                Draw.line(x + half_size, y, x + half_size, y - size)
            elif char == '2':
                Draw.line(x, y, x + size, y)  # top
                Draw.line(x, y - half_size, x, y - size)  #
                Draw.line(x, y - half_size, x + size, y - half_size)  # middle
                Draw.line(x + size, y, x + size, y - half_size)
                Draw.line(x, y - size, x + size, y - size)
            elif char == '3':
                Draw.line(x, y, x + size, y)
                Draw.line(x, y - half_size, x + size, y - half_size)
                Draw.line(x, y - size, x + size, y - size)
                Draw.line(x + size, y, x + size, y - size)
            elif char == '4':
                Draw.line(x, y, x, y - half_size)
                Draw.line(x, y - half_size, x + size, y - half_size)
                Draw.line(x + size, y, x + size, y - size)
            elif char == '5':
                Draw.line(x + size, y, x, y)
                Draw.line(x, y, x, y - half_size)
                Draw.line(x, y - half_size, x + size, y - half_size)
                Draw.line(x + size, y - half_size, x + size, y - size)
                Draw.line(x, y - size, x + size, y - size)
            elif char == '6':
                Draw.line(x + size, y, x, y)
                Draw.line(x, y, x, y - size)
                Draw.line(x, y - size, x + size, y - size)
                Draw.line(x + size, y - half_size, x, y - half_size)
                Draw.line(x + size, y - half_size, x + size, y - size)
            elif char == '7':
                Draw.line(x, y, x + size, y)
                Draw.line(x + size, y, x + size, y - size)
            elif char == '8':
                Draw.line(x, y, x, y - size)
                Draw.line(x, y, x + size, y)
                Draw.line(x + size, y, x + size, y - size)
                Draw.line(x, y - size, x + size, y - size)
                Draw.line(x, y - half_size, x + size, y - half_size)
            elif char == '9':
                Draw.line(x, y, x, y - half_size)  # left top vertical
                Draw.line(x, y, x + size, y)  # top
                Draw.line(x + size, y, x + size, y - size)
                Draw.line(x, y - size, x + size, y - size)
                Draw.line(x, y - half_size, x + size, y - half_size)  # middle

    @staticmethod
    def background(color: str):
        rgb = Draw.hex_to_rgb_normalized(color)
        glClearColor(rgb[0], rgb[1], rgb[2], 0.0)
