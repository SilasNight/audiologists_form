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
        text = -20
        label = self.side + " Ear"

        self.canvas.create_text(175, 10, text=label)
        self.canvas.create_text(175, 30, text="Frequency")
        self.canvas.create_text(10, 366, text="M", font=("Helvetica", 8, "bold"))

        for i in range(x_lines):
            step += step_y
            text += 10
            self.canvas.create_line(x_min, y_min + step, x_max, y_min + step)
            self.canvas.create_text(x_min - 20, y_min + step, text=str(text))

        step = 0
        text = 125

        for i in range(y_lines - 1):
            if i < 4:
                if i % 2 == 1:
                    step += step_x
                    continue

            if i % 2 == 0:
                self.canvas.create_line(x_min + step, y_min, x_min + step, y_max, width=2)
            else:
                self.canvas.create_line(x_min + step, y_min, x_min + step, y_max)

            self.canvas.create_text(x_min + step, y_min - 10, text=str(self.format_text(text)))
            text = self.change_text(text)
            step += step_x

    @staticmethod
    def change_text(text: int) -> int:
        if text < 500:
            text *= 2
        elif text < 1000:
            text += 250
        elif text < 1500:
            text += 500
        elif text < 4000:
            text += 1000
        else:
            text += 2000

        return text

    @staticmethod
    def format_text(text: int) -> str:
        if text >= 1000:
            if text == 1500:
                return "1.5K"
            else:
                text = str(text)
                char = text[:1]
                output = f"{char}K"
                return output
        else:
            text = str(text)
            return text

    def add_text(self):
        pass


