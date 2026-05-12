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
        self.scrolling_window = tk.Canvas(self.viewing_window, width=790, height=1500)
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

        # Start bottom bit
        self.bottom_canvas = tk.Canvas(self.scrolling_window)
        width = 750 - 5
        height = 350 - 5

        # Initialize bottom bit
        self.top_r = tk.Label(self.scrolling_window, text="R")
        self.top_l = tk.Label(self.scrolling_window, text="L")
        self.top_b = tk.Label(self.scrolling_window, text="B")
        self.masking = tk.Label(self.scrolling_window, text="Masking")
        self.low_r = tk.Label(self.scrolling_window, text="R")
        self.low_l = tk.Label(self.scrolling_window, text="L")
        self.low_b = tk.Label(self.scrolling_window, text="B")
        self.fourKHz = tk.Label(self.scrolling_window, text="4KHz")
        self.threeKHz = tk.Label(self.scrolling_window, text="3KHz")
        self.twoKHz = tk.Label(self.scrolling_window, text="2KHz")
        self.oneKHz = tk.Label(self.scrolling_window, text="1KHz")
        self.five_hundoHz = tk.Label(self.scrolling_window, text="500Hz")

        self.fourKHz_top = tk.Label(self.scrolling_window, text="4KHz")
        self.fourKHz_mid = tk.Label(self.scrolling_window, text="4KHz")
        self.fourKHz_bot = tk.Label(self.scrolling_window, text="4KHz")
        self.threeKHz_top = tk.Label(self.scrolling_window, text="3KHz")
        self.threeKHz_mid = tk.Label(self.scrolling_window, text="3KHz")
        self.threeKHz_bot = tk.Label(self.scrolling_window, text="3KHz")
        self.twoKHz_top = tk.Label(self.scrolling_window, text="2KHz")
        self.twoKHz_mid = tk.Label(self.scrolling_window, text="2KHz")
        self.twoKHz_bot = tk.Label(self.scrolling_window, text="2KHz")
        self.oneKHz_top = tk.Label(self.scrolling_window, text="1KHz")
        self.oneKHz_mid = tk.Label(self.scrolling_window, text="1KHz")
        self.oneKHz_bot = tk.Label(self.scrolling_window, text="1KHz")
        self.five_h_Hz_top = tk.Label(self.scrolling_window, text="500Hz")
        self.five_h_Hz_mid = tk.Label(self.scrolling_window, text="500Hz")
        self.five_h_Hz_bot = tk.Label(self.scrolling_window, text="500Hz")

        self.p_t_a = tk.Label(self.scrolling_window, text="Pure Tone Average")
        self.two_f_a = tk.Label(self.scrolling_window, text="2 Freq. Avg.")
        self.mcl = tk.Label(self.scrolling_window, text="MCL")
        self.ucl = tk.Label(self.scrolling_window, text="UCL")
        self.srt = tk.Label(self.scrolling_window, text="SRT")
        self.discrim_pipb = tk.Label(self.scrolling_window, text="Discrim.(PIPB)")
        self.rollover_yn = tk.Label(self.scrolling_window, text="Rollover(Y/N)")
        self.tone_decay = tk.Label(self.scrolling_window, text="Tone Decay")
        self.tympanometry = tk.Label(self.scrolling_window, text="Tympanometry")
        self.reflexes = tk.Label(self.scrolling_window, text="Reflexes Ipsilateral")
        self.contralatral_r = tk.Label(self.scrolling_window, text="Contaralateral R")
        self.reflex_decay_r = tk.Label(self.scrolling_window, text="Reflex Decay R")
        self.reflex_decay_l = tk.Label(self.scrolling_window, text="Reflex Decay L")
        self.p_t_a_r = tk.Entry(self.scrolling_window, bg="gray90")
        self.p_t_a_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.p_t_a_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.p_t_a_m = tk.Entry(self.scrolling_window, bg="gray90")
        self.two_f_a_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.two_f_a_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.two_f_a_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.two_f_a_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.mcl_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.mcl_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.mcl_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.mcl_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.ucl_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.ucl_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.ucl_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.ucl_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.srt_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.srt_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.srt_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.srt_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.discrim_pipb_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.discrim_pipb_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.discrim_pipb_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.discrim_pipb_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.rollover_yn_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.rollover_yn_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.rollover_yn_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.rollover_yn_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tone_decay_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tone_decay_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tone_decay_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tone_decay_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tympanometry_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tympanometry_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tympanometry_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.tympanometry_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflexes_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflexes_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflexes_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflexes_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.contralatral_r_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.contralatral_r_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.contralatral_r_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.contralatral_r_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_r_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_r_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_r_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_r_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_l_r = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_l_l = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_l_b = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        self.reflex_decay_l_m = tk.Entry(self.scrolling_window, width=10, bg="gray90")
        # End initialize bottom bit

        # Place bottom bit
        self.top_r.place(x=150, y=826)
        self.top_l.place(x=200, y=826)
        self.top_b.place(x=250, y=826)
        self.masking.place(x=425, y=826)
        self.low_r.place(x=50, y=840)
        self.low_l.place(x=100, y=840)
        self.low_b.place(x=150, y=840)
        self.fourKHz.place(x=200, y=840)
        self.threeKHz.place(x=50, y=855)
        self.twoKHz.place(x=100, y=855)
        self.oneKHz.place(x=150, y=855)
        self.five_hundoHz.place(x=200, y=855)

        self.fourKHz_top.place(x=50, y=870)
        self.fourKHz_mid.place(x=100, y=870)
        self.fourKHz_bot.place(x=150, y=870)
        self.threeKHz_top.place(x=200, y=870)
        self.threeKHz_mid.place(x=50, y=885)
        self.threeKHz_bot.place(x=100, y=885)
        self.twoKHz_top.place(x=150, y=885)
        self.twoKHz_mid.place(x=200, y=885)
        self.twoKHz_bot.place(x=50, y=900)
        self.oneKHz_top.place(x=100, y=900)
        self.oneKHz_mid.place(x=150, y=900)
        self.oneKHz_bot.place(x=200, y=900)
        self.five_h_Hz_top.place(x=50, y=915)
        self.five_h_Hz_mid.place(x=100, y=915)
        self.five_h_Hz_bot.place(x=150, y=915)

        self.p_t_a.place(x=200, y=915)
        self.two_f_a.place(x=50, y=930)
        self.mcl.place(x=100, y=930)
        self.ucl.place(x=150, y=930)
        self.srt.place(x=200, y=930)
        self.discrim_pipb.place(x=50, y=945)
        self.rollover_yn.place(x=100, y=945)
        self.tone_decay.place(x=150, y=945)
        self.tympanometry.place(x=200, y=945)
        self.reflexes.place(x=50, y=960)
        self.contralatral_r.place(x=100, y=960)
        self.reflex_decay_r.place(x=150, y=960)
        self.reflex_decay_l.place(x=200, y=960)
        self.p_t_a_r.place(x=50, y=975)  # self.p_t_a_r.place(x=425, y=849)
        self.p_t_a_l.place(x=100, y=975)
        self.p_t_a_b.place(x=150, y=975)
        self.p_t_a_m.place(x=425, y=849)  # self.p_t_a_m.place(x=200, y=975)
        self.two_f_a_r.place(x=50, y=990)
        self.two_f_a_l.place(x=100, y=990)
        self.two_f_a_b.place(x=150, y=990)
        self.two_f_a_m.place(x=200, y=990)
        self.mcl_r.place(x=50, y=1005)
        self.mcl_l.place(x=100, y=1005)
        self.mcl_b.place(x=150, y=1005)
        self.mcl_m.place(x=200, y=1005)
        self.ucl_r.place(x=50, y=1020)
        self.ucl_l.place(x=100, y=1020)
        self.ucl_b.place(x=150, y=1020)
        self.ucl_m.place(x=200, y=1020)
        self.srt_r.place(x=50, y=1035)
        self.srt_l.place(x=100, y=1035)
        self.srt_b.place(x=150, y=1035)
        self.srt_m.place(x=200, y=1035)
        self.discrim_pipb_r.place(x=50, y=1050)
        self.discrim_pipb_l.place(x=100, y=1050)
        self.discrim_pipb_b.place(x=150, y=1050)
        self.discrim_pipb_m.place(x=200, y=1050)
        self.rollover_yn_r.place(x=50, y=1065)
        self.rollover_yn_l.place(x=100, y=1065)
        self.rollover_yn_b.place(x=150, y=1065)
        self.rollover_yn_m.place(x=200, y=1065)
        self.tone_decay_r.place(x=50, y=1080)
        self.tone_decay_l.place(x=100, y=1080)
        self.tone_decay_b.place(x=150, y=1080)
        self.tone_decay_m.place(x=200, y=1080)
        self.tympanometry_r.place(x=50, y=1095)
        self.tympanometry_l.place(x=100, y=1095)
        self.tympanometry_b.place(x=150, y=1095)
        self.tympanometry_m.place(x=200, y=1095)
        self.reflexes_r.place(x=50, y=1110)
        self.reflexes_l.place(x=100, y=1110)
        self.reflexes_b.place(x=150, y=1110)
        self.reflexes_m.place(x=200, y=1110)
        self.contralatral_r_r.place(x=50, y=1125)
        self.contralatral_r_l.place(x=100, y=1125)
        self.contralatral_r_b.place(x=150, y=1125)
        self.contralatral_r_m.place(x=200, y=1125)
        self.reflex_decay_r_r.place(x=50, y=1140)
        self.reflex_decay_r_l.place(x=100, y=1140)
        self.reflex_decay_r_b.place(x=150, y=1140)
        self.reflex_decay_r_m.place(x=200, y=1140)
        self.reflex_decay_l_r.place(x=50, y=1155)
        self.reflex_decay_l_l.place(x=100, y=1155)
        self.reflex_decay_l_b.place(x=150, y=1155)
        self.reflex_decay_l_m.place(x=200, y=1155)

        self.create_lower_bit()
        # End place bottom bit
        # End bottom bit

        self.window.mainloop()

    def create_lower_bit(self):
        self.scrolling_window.create_line(15, 825, 765, 825)

        y = 0
        for i in range(25):
            y = 825 + (i * 22)
            self.scrolling_window.create_line(15, y, 550, y)

        print(y)
        self.scrolling_window.create_line(15, y, 765, y)
        # 422

        x = 0
        for i in range(5):
            x = 550 - (i * 128)
            self.scrolling_window.create_line(x, 825, x, 1353)
        self.scrolling_window.create_line(15, 825, 15, 1353)

    def y(self):
        self.y_ += 20
        return self.y_

    @staticmethod
    def locate(event):
        print(f"X = {event.x}")
        print(f"Y = {event.y}")

    def test(self, event):
        x = self.scrolling_window.winfo_x()
        y = self.scrolling_window.winfo_y()

        if event.delta > 1:
            if y != 0:
                self.scrolling_window.place_forget()
                y += 30
                self.scrolling_window.place(x=x, y=y)
        else:
            self.scrolling_window.place_forget()
            y -= 30
            self.scrolling_window.place(x=x, y=y)


if __name__ == "__main__":
    Ui()
