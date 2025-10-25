def shading(start_color, end_color, steps):
    """Returns a list of colors in #rrggbb form. They progress from
    start_color to end_color in the given number of steps."""

    hexes = [start_color[1:3], end_color[1:3], start_color[3:5], end_color[3:5], start_color[5:7], end_color[5:7]]

    """Converts all hex codes into integer numbers from 0 to 255.
    Stores them in the list nums"""
    nums = []
    for x in hexes:
        num10_from_num16 = int(x, base=16)
        nums.append(num10_from_num16)

    red_dist = nums[1] - nums[0]
    green_dist = nums[3] - nums[2]
    blue_dist = nums[5] - nums[4]

    """new_nums stores integer values (0-255) for the next color"""
    new_nums = [nums[0], nums[2], nums[4]]
    """color_list stores all of the colors in #rrggbb form"""
    color_list = [start_color]
    for x in range(steps):
        if x < red_dist % steps:
            red_change = red_dist // steps + 1
        else:
            red_change = red_dist // steps
        if x < green_dist % steps:
            green_change = green_dist // steps + 1
        else:
            green_change = green_dist // steps
        if x < blue_dist % steps:
            blue_change = blue_dist // steps + 1
        else:
            blue_change = blue_dist // steps
        new_nums[0] = new_nums[0] + red_change
        new_nums[1] = new_nums[1] + green_change
        new_nums[2] = new_nums[2] + blue_change

        """Converts from integer values into hex codes, formatted properly."""
        hex_code = '#'
        for y in new_nums:
            if y < 16:
                add_str = '0' + '%x' % y
            else:
                add_str = '%x' % y
            hex_code = hex_code + add_str
        color_list.append(hex_code)
    return color_list


import turtle

win = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

"""Draws a line that changes color."""
mycolors=shading('#fae3f2','#fa009e',100)
t.ht()
t.up()
t.goto(-300,0)
t.down()
t.color(mycolors[0])
t.width(8)
t.dot(15)
for x in mycolors:
    t.color(x)
    t.fd(600/len(mycolors))
t.color(mycolors[len(mycolors)-1])
t.dot(15)

"""Draws a circle that changes color."""
colors1=shading('#00edfa','#fa009e',90)
colors2=shading('#fa009e','#00edfa',90)
t.up()
t.goto(0,-200)
t.width(5)
t.down()
for x in colors1:
    t.color(x)
    t.circle(200,extent=2)
for x in colors2:
    t.color(x)
    t.circle(200,extent=2)

win.exitonclick()