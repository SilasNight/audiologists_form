class Grid:
    def __init__(self, canvas, side):
        """
        This function is to be used alongside an ui based in tkinter. This will make a grid for my audiogram
        :param canvas: The canvas that will be changed into a grid.
        :param side: Either Left or Right
        """
        self.canvas = canvas
        self.height = 380
        self.width = 350
        self.side = side
        self.update_settings()
        self.draw_lines()
        self.draw_grid()

    def update_settings(self):
        self.canvas.config(height=self.height, width=self.width, highlightthickness=0)
        self.canvas.update()

    def draw_lines(self):
        x = 0
        y = 0

        width = self.width - 1
        height = self.height - 1

        self.canvas.create_line(x, y, x + width, y)
        self.canvas.create_line(x, y, x, y + height)
        self.canvas.create_line(x, y + height, x + width + 1, y + height)
        self.canvas.create_line(x + width, y, x + width, y + height + 1)

        for i in range(3):
            y += 20
            self.canvas.create_line(x, y, x + width, y)

        self.canvas.create_line(x, height - 20, x + width, height - 20)
        self.canvas.create_line(35, 60, 35, height)

    def draw_grid(self):
        # 35, 60, 345, 360 , 13, 14
        x_min = 35
        x_max = 350
        y_min = 60
        y_max = 360
        x_lines = 13
        y_lines = 14

        dif_x = x_max - x_min
        dif_y = y_max - y_min
        step_x = dif_x/x_lines
        step_y = dif_y/y_lines

        step = 0

        for i in range(x_lines):
            step += step_y
            self.canvas.create_line(x_min, y_min + step, x_max, y_min + step)

        step = 0

        for i in range(y_lines):
            step += step_x
            self.canvas.create_line(x_min + step, y_min, x_min + step, y_max)

    def add_text(self):
        pass


