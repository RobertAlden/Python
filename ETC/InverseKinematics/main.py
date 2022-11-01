from graphics import *
from math import pi, sqrt, cos, sin
from library import *

scr_w = 1024
scr_h = 1024

values = drange(-pi, pi, (pi * 0.05))
values = [x for x in values]
values.append(0)
print(values)
max_length = 200


class Segment:
    def __init__(self, i, window):
        self.index = i
        self.window = window

        if self.index == 0:
            self.start_pos = Point(scr_w // 2, scr_h // 2)
            self.end_pos = Point(scr_w // 2, scr_h // 2)
            self.width = 4
            self.length = max_length // 2
        else:
            self.start_pos = Point(0, 0)
            self.end_pos = Point(0, 0)
            self.width = 4
            self.length = 80

        self.body = Line(self.start_pos, self.end_pos)
        self.body.setFill("red")
        self.body = self.body.draw(self.window)
        self.angle = -pi / 2
        self.magnitude = 1

    def update(self, segments, mx, my):
        results = [0] * len(values)

        for i, v in enumerate(values):
            self.angle += v * self.magnitude

            end_x = self.start_pos.getX() + p2c_x(self.length, self.angle)
            end_y = self.start_pos.getY() + p2c_y(self.length, self.angle)

            dx = end_x - self.end_pos.getX()
            dy = end_y - self.end_pos.getY()

            self.end_pos = Point(end_x, end_y)

            arm_end_point = segments[-1].body.getP2()
            arm_end_x = arm_end_point.getX() + dx
            arm_end_y = arm_end_point.getY() + dy

            results[i] = point_distance(arm_end_x, arm_end_y, mx, my)

            self.angle -= v * self.magnitude

            end_x = self.start_pos.getX() + p2c_x(self.length, self.angle)
            end_y = self.start_pos.getY() + p2c_y(self.length, self.angle)
            self.end_pos = Point(end_x, end_y)

        closest = results.index(min(results))
        self.angle += values[closest] * self.magnitude
        end_x = self.start_pos.getX() + p2c_x(self.length, self.angle)
        end_y = self.start_pos.getY() + p2c_y(self.length, self.angle)
        self.end_pos = Point(end_x, end_y)

        if min(results) < 100:
            self.magnitude = min(self.magnitude * .99, 0.1)
        else:
            self.magnitude = 1

        for s in segments[self.index:]:
            if s.index < len(segments) - 1:
                child = segments[s.index + 1]
                dx = s.end_pos.getX() - child.start_pos.getX()
                dy = s.end_pos.getY() - child.start_pos.getY()
                child.start_pos.move(dx, dy)
                child.end_pos.move(dx, dy)

    def draw(self):

        self.body.undraw()
        self.body = Line(self.start_pos, self.end_pos)
        self.body.setWidth(10 - self.index)
        self.body.setFill("red")
        self.body = self.body.draw(self.window)


def main():
    win = GraphWin("Inverse Kinematics", scr_w, scr_h, autoflush=False)
    win.setBackground("black")

    segments = []
    number_of_segments = 5
    for i in range(number_of_segments):
        segment = Segment(i, win)
        segments.append(segment)

    mouse_x = scr_w // 2
    mouse_y = scr_h // 2
    target = Circle(Point(mouse_x, mouse_y), 5)
    target.setOutline("green")
    target.draw(win)

    while(True):
        mouse_point = win.checkMouse()
        if mouse_point is not None:
            mouse_x = mouse_point.getX()
            mouse_y = mouse_point.getY()
            t_x = target.getCenter().getX()
            t_y = target.getCenter().getY()
            target.move(mouse_x - t_x, mouse_y - t_y)

        kb_input = win.checkKey()
        if kb_input != "":
            if kb_input == "q":
                break

        arm_end_point = segments[-1].body.getP2()
        arm_end_x = arm_end_point.getX()
        arm_end_y = arm_end_point.getY()
        error = point_distance(arm_end_x, arm_end_y, mouse_x, mouse_y)
        if error > 1:
            print(error)
            for s in reversed(segments):
                s.update(segments, mouse_x, mouse_y)
                s.draw()

        update(5)

    win.close()


if __name__ == "__main__":
    main()
