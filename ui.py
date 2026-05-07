import tkinter as tk
import grid


class Ui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Audiogram")
        self.window.config(bg="white")
        self.window.option_add("*Background", "white")
        self.window.geometry("800x800")
        icon = tk.PhotoImage(file="images/ear.png")
        self.window.iconphoto(True, icon)

        self.viewing_window = tk.Canvas(self.window, width=790, height=790)
        self.viewing_window.place(x=5, y=5)

        # Starting bindings
        self.window.bind_all("<MouseWheel>", lambda e: self.test(e))
        self.window.bind("<Button-3>", lambda e: self.locate(e))
        # End bindings

        # Initialize labels and entry for the first part
        self.scrolling_window = tk.Canvas(self.viewing_window, width=790, height=1000)
        self.dot_label = tk.Label(self.scrolling_window, text="Date of Test:", )
        self.dot_entry = tk.Entry(self.scrolling_window, bg="gray90")
        self.first_name_label = tk.Label(self.scrolling_window, text="First Name:")
        self.first_name_entry = tk.Entry(self.scrolling_window, width=50, bg="gray90")
        self.last_name_label = tk.Label(self.scrolling_window, text="Last Name:")
        self.last_name_entry = tk.Entry(self.scrolling_window, width=56, bg="gray90")
        self.dob_label = tk.Label(self.scrolling_window, text="DOB:")
        self.dob_entry = tk.Entry(self.scrolling_window, bg="gray90")
        self.age_label = tk.Label(self.scrolling_window, text="Age:")
        self.age_entry = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.id_label = tk.Label(self.scrolling_window, text="ID:")
        self.id_entry = tk.Entry(self.scrolling_window, width=30, bg="gray90")
        self.referred_by_label = tk.Label(self.scrolling_window, text="Referred By:")
        self.referred_by_Entry = tk.Entry(self.scrolling_window, width=30, bg="gray90")
        self.reason_label = tk.Label(self.scrolling_window, text="Reason:")
        self.reason_entry = tk.Entry(self.scrolling_window, width=34, bg="gray90")
        self.accompanied_by_label = tk.Label(self.scrolling_window, text="Accompanied By:")
        self.accompanied_by_entry = tk.Entry(self.scrolling_window, width=50, bg="gray90")
        self.relationship_label = tk.Label(self.scrolling_window, text="Relationship:")
        self.relationship_Entry = tk.Entry(self.scrolling_window, width=50, bg="gray90")
        self.physician_label = tk.Label(self.scrolling_window, text="Physician")  # This is a header
        self.p_first_name_label = tk.Label(self.scrolling_window, text="First Name:")
        self.p_first_name_entry = tk.Entry(self.scrolling_window, width=50, bg="gray90")
        self.p_last_name_label = tk.Label(self.scrolling_window, text="Last Name:")
        self.p_last_name_entry = tk.Entry(self.scrolling_window, width=56, bg="gray90")
        self.tested_by_label = tk.Label(self.scrolling_window, text="Tested By:")
        self.tested_by_entry = tk.Entry(self.scrolling_window, bg="gray90")
        self.hearing_label = tk.Label(self.scrolling_window, text="Hearing Aid Info")  # This is a header
        self.right_aid_label = tk.Label(self.scrolling_window, text="Right Aid:")
        self.right_aid_entry = tk.Entry(self.scrolling_window, width=121, bg="gray90")
        self.left_aid_label = tk.Label(self.scrolling_window, text="Left Aid:")
        self.left_aid_entry = tk.Entry(self.scrolling_window, width=121, bg="gray90")
        self.otoscopy_label = tk.Label(self.scrolling_window, text="Otoscopy")
        self.otoscopy_entry = tk.Text(self.scrolling_window, width=98, height=4, bg="gray90")  # Needs to be a big entry
        # End first initialize

        # Place starting labels and entry
        self.scrolling_window.place(x=0, y=0)
        self.y_ = 10 + (20*14)
        increment = 20
        y = 0
        self.dot_label.place(x=1, y=y)
        self.dot_entry.place(x=73, y=y)
        y += increment  # This is a new line
        y += increment
        self.first_name_label.place(x=1, y=y)
        self.first_name_entry.place(x=73, y=y)
        self.last_name_label.place(x=380, y=y)
        self.last_name_entry.place(x=450, y=y)
        y += increment
        self.dob_label.place(x=1, y=y)
        self.dob_entry.place(x=35, y=y)
        self.age_label.place(x=166, y=y)
        self.age_entry.place(x=200, y=y)
        self.referred_by_label.place(x=270, y=y)
        self.referred_by_Entry.place(x=342, y=y)
        self.reason_label.place(x=533, y=y)
        self.reason_entry.place(x=582, y=y)
        y += increment
        self.id_label.place(x=1, y=y)
        self.id_entry.place(x=20, y=y)
        y += increment
        y += increment
        self.accompanied_by_label.place(x=1, y=y)
        self.accompanied_by_entry.place(x=100, y=y)
        self.relationship_label.place(x=410, y=y)
        self.relationship_Entry.place(x=486, y=y)
        y += increment
        y += increment
        self.physician_label.place(x=1, y=y)
        y += increment
        self.p_first_name_label.place(x=1, y=y)
        self.p_first_name_entry.place(x=73, y=y)
        self.p_last_name_label.place(x=380, y=y)
        self.p_last_name_entry.place(x=450, y=y)
        y += increment
        y += increment
        self.tested_by_label.place(x=1, y=y)
        self.tested_by_entry.place(x=62, y=y)
        y += increment
        self.hearing_label.place(x=1, y=y)
        y += increment
        self.right_aid_label.place(x=1, y=y)
        self.right_aid_entry.place(x=60, y=y)
        y += increment
        self.left_aid_label.place(x=1, y=y)
        self.left_aid_entry.place(x=60, y=y)
        y += increment
        self.otoscopy_label.place(x=1, y=y)
        y += increment
        self.otoscopy_entry.place(x=1, y=y)
        # End place starting labels and entry

        # Start grids section
        self.right_grid = tk.Canvas(self.scrolling_window)
        self.left_grid = tk.Canvas(self.scrolling_window)

        self.r_control = grid.Grid(self.right_grid, side="Right")
        self.l_control = grid.Grid(self.left_grid, side="Left")

        self.right_grid.place(x=15, y=420)
        self.left_grid.place(x=415, y=420)

        # End grids section

        self.window.mainloop()

    def y(self):
        self.y_ += 20
        return self.y_

    @staticmethod
    def locate(event):
        print(f"X = {event.x}")
        print(f"Y = {event.y}")

    def test(self, event):
        if event.delta > 1:
            x = self.scrolling_window.winfo_x()
            y = self.scrolling_window.winfo_y()
            self.scrolling_window.place_forget()
            y += 5
            self.scrolling_window.place(x=x, y=y)
        else:
            x = self.scrolling_window.winfo_x()
            y = self.scrolling_window.winfo_y()
            self.scrolling_window.place_forget()
            y -= 5
            self.scrolling_window.place(x=x, y=y)


if __name__ == "__main__":
    Ui()
