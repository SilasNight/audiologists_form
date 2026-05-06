import tkinter as tk


class Ui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Audiogram")
        self.window.config(bg="white")
        self.window.option_add("*Background", "white")
        self.window.geometry("800x800")
        self.viewing_window = tk.Canvas(self.window, width=790, height=790)
        self.viewing_window.place(x=5, y=5)

        # Starting bindings
        self.window.bind_all("<MouseWheel>", lambda e: self.test(e))
        # End bindings


        # Initialize labels and entry for the first part
        self.scrolling_window = tk.Canvas(self.viewing_window, width=790, height=1000)
        self.dot_label = tk.Label(self.scrolling_window, text="Date of Test:", )
        self.dot_entry = tk.Entry(self.scrolling_window)
        self.first_name_label = tk.Label(self.scrolling_window, text="First Name:")
        self.first_name_entry = tk.Entry(self.scrolling_window)
        self.last_name_label = tk.Label(self.scrolling_window, text="Last Name:")
        self.last_name_entry = tk.Entry(self.scrolling_window)
        self.dob_label = tk.Label(self.scrolling_window, text="DOB:")
        self.dob_entry = tk.Entry(self.scrolling_window)
        self.age_label = tk.Label(self.scrolling_window, text="Age:")
        self.referred_by_label = tk.Label(self.scrolling_window, text="Referred By")
        self.referred_by_Entry = tk.Entry(self.scrolling_window)
        self.reason_label = tk.Label(self.scrolling_window, text="Reason:")
        self.reason_entry = tk.Entry(self.scrolling_window)
        self.accompanied_by_label = tk.Label(self.scrolling_window, text="Accompanied By:")
        self.accompanied_by_entry = tk.Entry(self.scrolling_window)
        self.relationship_label = tk.Label(self.scrolling_window, text="Relationship:")
        self.relationship_Entry = tk.Entry(self.scrolling_window)
        self.physician_label = tk.Label(self.scrolling_window, text="Physician")  # This is a header
        self.p_first_name_label = tk.Label(self.scrolling_window, text="First Name:")
        self.p_first_name_entry = tk.Entry(self.scrolling_window)
        self.p_last_name_label = tk.Label(self.scrolling_window, text="Last Name:")
        self.p_last_name_entry = tk.Entry(self.scrolling_window)
        self.tested_by_label = tk.Label(self.scrolling_window, text="Tested By:")
        self.tested_by_entry = tk.Entry(self.scrolling_window, )
        self.id_label = tk.Label(self.scrolling_window, text="ID:")
        self.id_entry = tk.Entry(self.scrolling_window)
        self.hearing_label = tk.Label(self.scrolling_window, text="Hearing Aid Info")  # This is a header
        self.right_aid_label = tk.Label(self.scrolling_window, text="Right Aid:")
        self.right_aid_entry = tk.Entry(self.scrolling_window)
        self.left_aid_label = tk.Label(self.scrolling_window, text="Left Aid:")
        self.left_aid_entry = tk.Entry(self.scrolling_window)
        self.otoscopy_label = tk.Label(self.scrolling_window, text="Otoscopy")
        self.otoscopy_entry = tk.Entry(self.scrolling_window)  # Needs to be a big entry
        # End first initialize

        # Place starting labels and entry
        self.scrolling_window.place(x=0, y=0)
        self.y_ = 10 + (20*2)
        self.dot_label.place(x=1, y=0)
        self.dot_entry.place(x=73, y=0)
        self.first_name_label.place(x=1, y=20)
        self.first_name_entry.place(x=73, y=20)
        self.last_name_label.place(x=200, y=20)
        self.last_name_entry.place(x=280, y=20)
        self.dob_label.place(x=1, y=self.y())
        self.dob_entry.place(x=1, y=self.y())
        self.age_label.place(x=1, y=self.y())
        self.referred_by_label.place(x=1, y=self.y())
        self.referred_by_Entry.place(x=1, y=self.y())
        self.reason_label.place(x=1, y=self.y())
        self.reason_entry.place(x=1, y=self.y())
        self.accompanied_by_label.place(x=1, y=self.y())
        self.accompanied_by_entry.place(x=1, y=self.y())
        self.relationship_label.place(x=1, y=self.y())
        self.relationship_Entry.place(x=1, y=self.y())
        self.physician_label.place(x=1, y=self.y())
        self.p_first_name_label.place(x=1, y=self.y())
        self.p_first_name_entry.place(x=1, y=self.y())
        self.p_last_name_label.place(x=1, y=self.y())
        self.p_last_name_entry.place(x=1, y=self.y())
        self.tested_by_label.place(x=1, y=self.y())
        self.tested_by_entry.place(x=1, y=self.y())
        self.id_label.place(x=1, y=self.y())
        self.id_entry.place(x=1, y=self.y())
        self.hearing_label.place(x=1, y=self.y())
        self.right_aid_label.place(x=1, y=self.y())
        self.right_aid_entry.place(x=1, y=self.y())
        self.left_aid_label.place(x=1, y=self.y())
        self.left_aid_entry.place(x=1, y=self.y())
        self.otoscopy_label.place(x=1, y=self.y())
        self.otoscopy_entry.place(x=1, y=self.y())

        self.window.mainloop()

    def y(self):
        self.y_ += 20
        return self.y_

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
