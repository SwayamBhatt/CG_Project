import turtle as te
from typing import Tuple

WriteSteps = 500        # Bezier function sampling times
Speed = 1
Width = 600             # Width of Interface
Height = 500            # Height of Interface
Xh, Yh = 0, 0           # Handle of the previous Bessel function used


te.tracer(10)
te.setup(Width, Height, 0, 0)
te.setworldcoordinates(0, Height, Width, 0)
te.pensize(1)
te.speed(Speed)
te.penup()


def move_to(point):
    te.penup()
    te.goto(point)


def bezier_point(points, timestep, dimension=2):
    degree = len(points) - 1
    if(degree == 0):
        return points[0]
    else:
        new_points = []
        for idx in range(degree):
            temp = []
            for d in range(dimension):
                temp.append(points[idx][d] * (1.0 - timestep) +
                            points[idx + 1][d] * timestep)
            new_points.append(tuple(temp))
        return bezier_point(tuple(new_points), timestep, dimension)


def bezier_curve(points, dimension=None):
    if(dimension is None):
        dimension = len(points[0])

    move_to(points[0])
    te.pendown()
    for timestep in range(0, WriteSteps + 1):
        p = bezier_point(points, timestep / WriteSteps, dimension)
        te.goto(p)
    te.penup()


def bezier_curve_through(points, relative: bool = False):
    global Xh
    global Yh
    curr = te.position()
    points = list(points)
    if(relative):
        for i in range(len(points)):
            points[i] = tuple([c1 + c2 for c1, c2 in zip(points[i], curr)])
    points.insert(0, curr)
    bezier_curve(tuple(points))
    Xh = points[-1][0] - points[-2][0]
    Yh = points[-1][1] - points[-2][1]


def smooth_bezier_curve(points, relative: bool = False):
    global Xh
    global Yh
    points = list(points)
    points.insert(0, (Xh + te.position()[0], Yh + te.position()[1]))
    if(relative):
        points[0] = (points[0][0] - te.position()[0],
                     points[0][1] - te.position()[1])
    bezier_curve_through(tuple(points), relative)

# Given two points; source and destination, draw a line connecting source to destination

def line_between(source, destination):
    move_to(source)
    te.pendown()
    te.goto(destination)

# Given certain displacement, draw a line from the current position to the displaced position.

def line_displace(displacement):
    line_between(te.position(), te.position() + displacement)

# Given the destination point, draw a line from the current position to that destination

def line_to(destination):
    line_between(te.position(), destination)
    
# Takes a destination x coordinate and draws a horizontal line from current position to destination point.

def horizontal_to(destination_x):
    line_between(te.position(), (destination_x, te.ycor()))

# Displacement in x-direction and draw the line

def horizontal_displace(dx):
    line_between(te.position(), te.position() + (dx, 0))

# # Displacement in y-direction and draw the line

def vertical_displace(dy):
    line_between(te.position(), te.position() + (0, dy))


def polyline(points):
    total = len(points)
    for idx in range(total - 1):
        line_between(points[idx], points[idx + 1])


def main():
    """
    Layer 1
    """

    # Code for Coat
    te.color("black", "#bf1717")
    move_to((61, 462))
    te.begin_fill()
    smooth_bezier_curve(((12, -41), (27, -58)), relative=True)
    bezier_curve_through(((-6, -36), (6, -118), (9, -132)), relative=True)
    bezier_curve_through(((-15, -27), (-23, -51), (-26, -74)), relative=True)
    bezier_curve_through(((4, -66), (38, -105), (65, -149)), relative=True)
    horizontal_to(486)
    bezier_curve_through(((12, 24), (40, 99), (33, 114)), relative=True)
    bezier_curve_through(((39, 82), (55, 129), (39, 144)), relative=True)
    smooth_bezier_curve(((-31, 23), (-39, 28)), relative=True)
    smooth_bezier_curve(((-12, 37), (-12, 37)), relative=True)
    line_displace((50, 92))
    horizontal_to(445)
    smooth_bezier_curve(((-29, -38), (-31, -46)), relative=True)
    smooth_bezier_curve(((78, -107), (72, -119)), relative=True)
    smooth_bezier_curve(((355, 178), (340, 176)))
    smooth_bezier_curve(((272, 63), (264, 64)))
    smooth_bezier_curve(((-29, 67), (-27, 73)), relative=True)
    smooth_bezier_curve(((99, 292), (174, 428), (173, 439)))
    smooth_bezier_curve(((-8, 23), (-8, 23)), relative=True)
    line_to((61, 462))
    te.end_fill()

    # Shadow
    move_to((60.5, 461.5))
    te.color("black", "#156deb")
    te.begin_fill()
    bezier_curve_through(((0, 0), (17, -42), (27, -59)), relative=True)
    bezier_curve_through(((-6, -33), (6, -128), (10, -133)), relative=True)
    bezier_curve_through(
        ((-15, -10), (-27, -66), (-27.285, -75)), relative=True)
    te.pencolor("#D3DFF0")
    bezier_curve_through(((12.285, 11), (82.963, 156),
                         (82.963, 156)), relative=True)
    te.pencolor("black")
    smooth_bezier_curve(((12.322, 75), (19.322, 86)), relative=True)
    bezier_curve_through(((-1, 11), (-8, 25), (-8, 25)), relative=True)
    horizontal_to(60.5)
    te.end_fill()

    move_to((444.5, 464))
    te.begin_fill()
    bezier_curve_through(((0, 0), (-29, -36), (-31, -46)), relative=True)
    smooth_bezier_curve(((53.59, -82.337), (53.59, -82.337)), relative=True)
    te.pencolor("#D3DFF0")
    smooth_bezier_curve(((86.41, -47.663), (96.072, -54.85)), relative=True)
    smooth_bezier_curve(((563.5, 297.5), (570.5, 299.5), (518.5, 334)))
    te.pencolor("black")
    bezier_curve_through(((-2, 16), (-12, 33), (-12, 37)), relative=True)
    smooth_bezier_curve(((50, 92), (50, 93)), relative=True)
    horizontal_to(444.5)
    te.end_fill()

    move_to((195, 49))
    te.begin_fill()
    te.pencolor("#D3DFF0")
    polyline(((195, 49), (175.5, 106.5), (202.522, 49)))
    te.pencolor("black")
    horizontal_to(195)
    te.pencolor("#D3DFF0")
    te.end_fill()

    move_to((327.997, 49))
    te.begin_fill()
    te.pencolor("#D3DFF0")
    bezier_curve_through(
        ((0, 0), (11.503, 121.087), (13.503, 128.087)), relative=True)
    bezier_curve_through(((11, 2), (54, 37), (54, 37)), relative=True)
    line_displace((-40, - 165.087))
    te.pencolor("black")
    horizontal_to(327.997)
    te.pencolor("#D3DFF0")
    te.end_fill()

    # Wrinkles
    te.pencolor("black")
    line_between((94.5, 397.5), (107.5, 373.5))
    line_between((122.5, 317.5), (95.875, 274.699))
    line_between((122.5, 341.5), (141.5, 402.5))
    line_between((141.5, 409.5), (153.5, 431.5))
    line_between((340.023, 49), (360.5, 144))
    line_between((478.5, 95.5), (518.5, 161.5))
    line_between((518.5, 332.5), (460.5, 359.5))
    polyline(((506.5, 369.5), (493.5, 402.5), (502.5, 443.5)))
    move_to((530, 429))
    bezier_curve_through(((4, 16), (-5, 33), (-5, 33)), relative=True)

    """
    Layer 2
    """

    # Inside of jacket
    te.color("black", "#d618c9")
    move_to((225, 462))
    te.begin_fill()
    horizontal_to(165)
    smooth_bezier_curve(((9, -15), (8, -25)), relative=True)
    bezier_curve_through(((-47, -126), (6, -212), (12, -225)), relative=True)
    smooth_bezier_curve(((185, 305), (202, 428), (225, 462)))
    line_to((225, 462))
    te.end_fill()

    move_to((390, 462))
    te.begin_fill()
    bezier_curve_through(
        ((10, -23), (34, -180), (35, -222)), relative=True)
    bezier_curve_through(((7, 4), (54, 45), (61, 61)), relative=True)
    smooth_bezier_curve(((-73, 101), (-72, 118)), relative=True)
    bezier_curve_through(((5, 15), (31, 46), (31, 45)), relative=True)
    line_to((390, 462))
    te.end_fill()

    """
    Layer 3
    """

    # Inside of jacket
    te.color("black", "#23660e")
    move_to((225, 462))
    te.begin_fill()
    bezier_curve_through(((-28, -50), (-40, -166), (-40, -250)), relative=True)
    bezier_curve_through(((6, 51), (-6, 87), (45, 106)), relative=True)
    smooth_bezier_curve(((64, 27), (89, 24)), relative=True)
    smooth_bezier_curve(((49, -18), (56, -20)), relative=True)
    smooth_bezier_curve(((50, -10), (51, -85)), relative=True)
    bezier_curve_through(((0, 29), (-25, 201), (-36, 225)), relative=True)
    line_to((225, 462))
    te.end_fill()

    """
    Layer 4
    """

    # Clothes
    te.color("black", "#d2f50c")
    move_to((225, 462))
    te.begin_fill()
    bezier_curve_through(((-5, -5), (-22, -53), (-23, -70)), relative=True)
    line_displace((32, -13))
    bezier_curve_through(((3, -25), (6, -28), (12, -36)), relative=True)
    smooth_bezier_curve(((13, -12), (16, -12)), relative=True)
    vertical_displace(-2)
    bezier_curve_through(((45, 20), (64, 14), (94, 1)), relative=True)
    vertical_displace(2)
    bezier_curve_through(((8, -2), (15, 2), (17, 4)), relative=True)
    smooth_bezier_curve(((0, 6), (-2, 9)), relative=True)
    bezier_curve_through(((10, 10), (10, 29), (11, 33)), relative=True)
    smooth_bezier_curve(((23, 4), (25, 6)), relative=True)
    smooth_bezier_curve(((-17, 83), (-17, 78)), relative=True)
    line_to((225, 462))
    te.end_fill()

    """
    Layer 5
    """

    # Neck
    te.color("black", "#09d6a6")
    move_to((262, 329))
    te.begin_fill()
    vertical_displace(17)
    bezier_curve_through(((1, 2), (44, 14), (45, 15)), relative=True)
    smooth_bezier_curve(((3, 12), (3, 12)), relative=True)
    horizontal_displace(3)
    vertical_displace(-5)
    bezier_curve_through(((1, -3), (4, -6), (5, -7)), relative=True)
    line_displace((36, -14))
    bezier_curve_through(((1, -1), (3, -16), (2, -17)), relative=True)
    smooth_bezier_curve(((318, 348), (296, 344), (262, 329)))
    te.end_fill()

    """
    Layer 6
    """

    # folds
    te.color("black", "#00070f")
    move_to((225, 462))
    te.begin_fill()
    line_displace((-3, - 5))
    bezier_curve_through(((0, -2), (4, -4), (5, -6)), relative=True)
    smooth_bezier_curve(((16, 3), (19, -8)), relative=True)
    smooth_bezier_curve(((0, -7), (0, -11)), relative=True)
    smooth_bezier_curve(((5, -8), (9, -5)), relative=True)
    smooth_bezier_curve(((19, -8), (19, -11)), relative=True)
    smooth_bezier_curve(((6, -7), (6, -7)), relative=True)
    smooth_bezier_curve(((7, -2), (9, -4)), relative=True)
    line_displace((41, -2))
    line_displace((12, 9))
    smooth_bezier_curve(((3, 15), (7, 18)), relative=True)
    smooth_bezier_curve(((15, 4), (17, 4)), relative=True)
    smooth_bezier_curve(((4, -4), (6, -4)), relative=True)
    smooth_bezier_curve(((6, 4), (5, 9)), relative=True)
    smooth_bezier_curve(((0, 9), (0, 9)), relative=True)
    smooth_bezier_curve(((1, 7), (7, 6)), relative=True)
    smooth_bezier_curve(((8, 0), (8, 0)), relative=True)
    line_displace((-2, 8))
    line_to((225, 462))
    te.end_fill()

    te.pensize(2)
    move_to((240, 450))
    smooth_bezier_curve(((0, 9), (3, 12)), relative=True)
    move_to((372, 462))
    bezier_curve_through(((-2, -4), (-5, -29), (-7, -28)), relative=True)
    te.pensize(1)

    """
    Layer 7
    """

    # Collar
    te.color("black", "#bd24b3")
    move_to((262, 331))
    te.begin_fill()
    bezier_curve_through(((0, 8), (-1, 13), (0, 15)), relative=True)
    smooth_bezier_curve(((43, 14), (45, 15)), relative=True)
    line_displace((3, 12))
    horizontal_displace(3)
    smooth_bezier_curve(((-1, -3), (0, -5)), relative=True)
    line_displace((5, -7))
    line_displace((36, -14))
    bezier_curve_through(((1, -1), (2, -12), (2, -15)), relative=True)
    smooth_bezier_curve(((25, -2), (15, 13)), relative=True)
    bezier_curve_through(((-2, 4), (-7, 29), (-7, 32)), relative=True)
    smooth_bezier_curve(((-35, 19), (-41, 22)), relative=True)
    smooth_bezier_curve(((-9, 14), (-12, 14)), relative=True)
    smooth_bezier_curve(((-7, -12), (-14, -15)), relative=True)
    bezier_curve_through(((-19, -2), (-41, -25), (-41, -25)), relative=True)
    smooth_bezier_curve(((-10, -26), (-10, -30)), relative=True)
    smooth_bezier_curve(((255, 332), (262, 331)))
    te.end_fill()

    move_to((262, 346))
    line_displace((-12, -6))
    move_to((369, 333))
    bezier_curve_through(((2, 4), (-6, 10), (-15, 14)), relative=True)

    """
    Layer 8
    """

    # Tie
    te.color("black", "#f5f5f5")
    move_to((247, 358))
    te.begin_fill()
    bezier_curve_through(((-5, 3), (-8, 20), (-6, 23)), relative=True)
    bezier_curve_through(((25, 21), (50, 17), (50, 17)), relative=True)
    line_displace((-23, 64))
    horizontal_displace(22)
    smooth_bezier_curve(((1, -13), (2, -16)), relative=True)
    line_displace((13, -50))
    bezier_curve_through(((2, 2), (7, 3), (10, 1)), relative=True)
    smooth_bezier_curve(((18, 65), (18, 65)), relative=True)
    horizontal_displace(19)
    line_displace((-24, -65))
    bezier_curve_through(((21, 5), (39, -10), (44, -13)), relative=True)
    bezier_curve_through(((5, -20), (1, -21), (0, -24)), relative=True)
    bezier_curve_through(((-18, -2), (-49, 15), (-52, 17)), relative=True)
    smooth_bezier_curve(((-11, -3), (-15, -1)), relative=True)
    smooth_bezier_curve(((252, 356), (247, 358)))
    te.end_fill()

    """
    Layer 9
    """

    # Collar visible through tie
    te.color("black", "#166bde")
    move_to((297, 387))
    te.begin_fill()
    line_displace((-11, 6))
    bezier_curve_through(((-1, 0), (-20, -7), (-30, -19)), relative=True)
    smooth_bezier_curve(((259, 373), (297, 385), (297, 387)))
    te.end_fill()

    move_to((323, 384))
    te.begin_fill()
    line_displace((8, 7))
    line_displace((30, -14))
    bezier_curve_through(((1, -1), (5, -6), (4, -7)), relative=True)
    smooth_bezier_curve(((329, 379), (323, 384)))
    te.end_fill()

    """
    Layer 10
    """

    # Face
    te.color("black", "#f2cfbb")
    move_to((185, 212))
    te.begin_fill()
    bezier_curve_through(((4, -9), (46, -77), (52, -75)), relative=True)
    bezier_curve_through(((-2, -17), (19, -68), (27, -73)), relative=True)
    bezier_curve_through(((16, 15), (71, 108), (76, 112)), relative=True)
    smooth_bezier_curve(((76, 53), (86, 60)), relative=True)
    bezier_curve_through(((0, 65), (-27, 75), (-31, 76)), relative=True)
    bezier_curve_through(((-50, 28), (-70, 30), (-85, 30)), relative=True)
    smooth_bezier_curve(((-77, -22), (-86, -26)), relative=True)
    smooth_bezier_curve(((180, 302), (186, 228), (185, 212)))
    te.end_fill()

    """
    Layer 11
    """

    # Hair
    te.color("black", "#a3178f")
    move_to((189, 202))
    te.begin_fill()
    bezier_curve_through(((-1, 22), (19, 51), (19, 51)), relative=True)
    smooth_bezier_curve(((-10, -42), (7, -92)), relative=True)
    smooth_bezier_curve(((212, 168), (196, 189), (189, 202)))
    te.end_fill()

    move_to((221, 155))
    te.begin_fill()
    bezier_curve_through(((-2, 6), (5, 48), (5, 48)), relative=True)
    smooth_bezier_curve(((18, -28), (20, -48)), relative=True)
    bezier_curve_through(((-5, 24), (4, 43), (7, 50)), relative=True)
    bezier_curve_through(((-10, -49), (3, -72), (13, -106)), relative=True)
    bezier_curve_through(((-2, -7), (-3, -32), (-3, -35)), relative=True)
    bezier_curve_through(((-17, 18), (-27, 71), (-27, 71)), relative=True)
    line_to((221, 155))
    te.end_fill()

    move_to((264, 64))
    te.begin_fill()
    bezier_curve_through(((-4, 5), (14, 100), (14, 100)), relative=True)
    smooth_bezier_curve(((-6, -79), (-5, -85)), relative=True)
    bezier_curve_through(((0, 98), (49, 139), (49, 139)), relative=True)
    smooth_bezier_curve(((8, -50), (3, -65)), relative=True)
    smooth_bezier_curve(((272, 64), (264, 64)))
    te.end_fill()

    move_to((342, 176))
    te.begin_fill()
    bezier_curve_through(((-1, 27), (-10, 57), (-10, 57)), relative=True)
    smooth_bezier_curve(((20, -33), (17, -54)), relative=True)
    line_to((342, 176))
    te.end_fill()

    te.penup()
    te.begin_fill()
    polyline(((349, 180), (353, 203), (361, 203)))
    polyline(((361, 203), (362, 188), (349, 180)))
    te.end_fill()

    """
    Layer 12
    """

    # Eyerbrows
    te.pensize(2)
    move_to((210, 180))
    bezier_curve_through(((5, -4), (63, 9), (63, 14)), relative=True)
    move_to((338, 193))
    bezier_curve_through(((0, -3), (18, -6), (18, -6)), relative=True)
    te.pensize(1)

    """
    Layer 13
    """

    # Eye 1
    te.color("black", "#f70707")
    te.pensize(2)
    move_to((206, 212))
    te.begin_fill()
    line_displace((15, -7))
    bezier_curve_through(((4, -1), (26, -2), (30, 0)), relative=True)
    smooth_bezier_curve(((10, 3), (12, 7)), relative=True)
    te.pencolor("#D1D1D1")
    te.pensize(1)
    smooth_bezier_curve(((2, 27), (-1, 30)), relative=True)
    smooth_bezier_curve(((-39, 5), (-44, 1)), relative=True)
    smooth_bezier_curve(((206, 212), (206, 212)))
    te.end_fill()

    move_to((384, 204))
    te.begin_fill()
    te.pencolor("black")
    te.pensize(2)
    bezier_curve_through(((-3, -1), (-18, -1), (-28, 1)), relative=True)
    smooth_bezier_curve(((-9, 6), (-10, 9)), relative=True)
    te.pencolor("#D1D1D1")
    te.pensize(1)
    smooth_bezier_curve(((3, 18), (6, 23)), relative=True)
    smooth_bezier_curve(((38, 6), (40, 4)), relative=True)
    smooth_bezier_curve(((10, -9), (13, -22)), relative=True)
    te.pencolor("black")
    te.pensize(2)
    line_to((384, 204))
    te.end_fill()

    """
    Layer 14
    """

    # Eye 2
    te.color("#0c3122", "#0c3122")
    te.pensize(1)
    move_to((216, 206))
    te.begin_fill()
    bezier_curve_through(((-1, 5), (0, 26), (7, 35)), relative=True)
    smooth_bezier_curve(((30, 2), (33, 0)), relative=True)
    smooth_bezier_curve(((5, -31), (2, -34)), relative=True)
    smooth_bezier_curve(((219, 203), (216, 206)))
    te.end_fill()

    move_to((354, 207))
    te.begin_fill()
    bezier_curve_through(((-2, 1), (2, 29), (4, 31)), relative=True)
    smooth_bezier_curve(((30, 3), (33, 1)), relative=True)
    smooth_bezier_curve(((6, -24), (4, -27)), relative=True)
    line_displace((-11, -8))
    smooth_bezier_curve(((382, 204), (357, 206), (354, 207)))
    te.end_fill()

    """
    Layer 15
    """

    # Eye 3
    te.color("#F5F5F5", "#F5F5F5")
    move_to((253, 211))
    te.begin_fill()
    bezier_curve_through(((-3, 0), (-8, 8), (1, 10)), relative=True)
    smooth_bezier_curve(((258, 210), (253, 211)))
    te.end_fill()

    move_to((392, 209))
    te.begin_fill()
    line_displace((4, 3))
    vertical_displace(4)
    line_displace((-4, 2))
    smooth_bezier_curve(((386, 214), (392, 209), (392, 209)))
    te.end_fill()

    """
    Layer 16
    """

    # Eye 4
    te.color("#352F53", "#352F53")
    move_to((219, 229))
    te.begin_fill()
    smooth_bezier_curve(((2, -5), (6, -4)), relative=True)
    smooth_bezier_curve(((18, 13), (27, 1)), relative=True)
    bezier_curve_through(((3, 0), (5, 3), (5, 3)), relative=True)
    vertical_displace(13)
    horizontal_to(224)
    line_to((219, 229))
    te.end_fill()

    move_to((357, 227))
    te.begin_fill()
    smooth_bezier_curve(((4, -6), (10, -2)), relative=True)
    smooth_bezier_curve(((10, 13), (19, 1)), relative=True)
    bezier_curve_through(((6, 0), (8, 6), (8, 6)), relative=True)
    line_displace((-2, 9))
    bezier_curve_through(((-12, 3), (-29, 0), (-32, -2)), relative=True)
    smooth_bezier_curve(((357, 227), (357, 227)))
    te.end_fill()

    """
    Layer 17
    """

    # Eye 5
    te.color("#9A90CB", "#9A90CB")
    move_to((227, 231))
    te.begin_fill()
    bezier_curve_through(((-6, 0), (-5, 5), (-3, 8)), relative=True)
    smooth_bezier_curve(((24, 2), (27, 0)), relative=True)
    smooth_bezier_curve(((0, -8), (-1, -8)), relative=True)
    smooth_bezier_curve(((234, 231), (227, 231)))
    te.end_fill()

    move_to((361, 227))
    te.begin_fill()
    bezier_curve_through(((2, 18), (26, 14), (30, 6)), relative=True)
    smooth_bezier_curve(((-1, -3), (-2, -4)), relative=True)
    smooth_bezier_curve(((-15, 9), (-24, -4)), relative=True)
    smooth_bezier_curve(((363, 224), (361, 225), (361, 227)))
    te.end_fill()

    """
    Layer 18
    """

    # Eye line
    te.pencolor("black")
    te.pensize(3)
    move_to((225, 215))
    bezier_curve_through(((10, 28), (22, 16), (24, 6)), relative=True)
    move_to((365, 219))
    bezier_curve_through(((4, 14), (18, 24), (22, -3)), relative=True)
    te.pensize(2)
    line_between((240.5, 207.5), (227.5, 211.5))
    line_between((245.5, 209.5), (227.5, 214.5))
    line_between((247.5, 211.5), (227.5, 217.5))
    line_between((247.5, 214.5), (229.5, 220.5))
    line_between((247.5, 218.5), (230.5, 223.5))
    line_between((246.5, 222.5), (232.5, 226.5))
    line_between((244.5, 225.5), (234.5, 228.5))
    line_between((377.5, 207.5), (367.5, 210.5))
    line_between((384.5, 207.5), (366.5, 212.5))
    line_between((385.5, 210.5), (366.5, 215.5))
    line_between((384.5, 213.5), (366.5, 218.5))
    line_between((384.5, 215.5), (367.5, 220.5))
    line_between((384.5, 218.5), (368.5, 223.5))
    line_between((382.5, 223.5), (370.5, 227.5))

    """
    Layer 19
    """

    # Nose and mouth
    te.pencolor("black")
    move_to((309, 270))
    bezier_curve_through(((0, 0), (4, 7), (1, 9)), relative=True)
    line_between((296.5, 307.5), (303.5, 307.5))
    move_to((315, 307))
    smooth_bezier_curve(((10, -1), (10, 2)), relative=True)

    # Wait for the user to click to exit
    te.exitonclick()


if __name__ == '__main__':
    main()
