# !usr/bin/env/python3
# -*- coding - utf-8 -*-
# ************************************************************************
# History      : ver1.0 kiiisy 2024/xx/xx Create New
# Discription  : gui process
# ************************************************************************
# Imports
# ************************************************************************
import customtkinter

from jenkins_module import my_jenkins


TAB_VIEW_NAME1 = "Create new job"
TAB_VIEW_NAME2 = "Edit job"
TAB_VIEW_NAME3 = "Create AutoSim job"
TAB_VIEW_NAME4 = "Config"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.fonts = ("helvetica", 20)
        self.fonts2 = ("helvetica", 15)

        # サイズ設定
        self.geometry(f"{1200}x{650}")
        self.title("Pykins")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # GUI生成
        self.setup_form()

    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # タブビューフレーム
        tabview = customtkinter.CTkTabview(self, corner_radius=10)
        tabview.grid(row=1, column=1, padx=(15, 15), pady=(0, 0), sticky="ew")
        tabview.add(TAB_VIEW_NAME1)
        tabview.add(TAB_VIEW_NAME2)
        tabview.add(TAB_VIEW_NAME3)
        tabview.add(TAB_VIEW_NAME4)
        tabview.tab(TAB_VIEW_NAME1).grid_columnconfigure(0, weight=1)
        tabview.tab(TAB_VIEW_NAME2).grid_columnconfigure(0, weight=1)
        tabview.tab(TAB_VIEW_NAME3).grid_columnconfigure(0, weight=1)
        tabview.tab(TAB_VIEW_NAME4).grid_columnconfigure(0, weight=1)

        # スクロールバーフレーム(job一覧)
        self.job_look_frame = JobLookFrame(master=self, font=self.fonts2,
                                           width=130, height=500, corner_radius=10,
                                           label_text="job一覧", label_font=self.fonts, label_fg_color="DodgerBlue3")
        self.job_look_frame.grid(row=1, column=2, padx=(5, 5), pady=(15, 15), sticky="ew")

        # タブビュー(Create new job)
        self.input_job_frame = InputJobFrame(tabview.tab(TAB_VIEW_NAME1), self.fonts)
        self.input_job_frame.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsew")

        self.build_day_frame = BuildDayFrame(tabview.tab(TAB_VIEW_NAME1), self.fonts)
        self.build_day_frame.grid(row=1, column=0, padx=10, pady=(10,10), sticky="nsew")

        self.build_time_frame = BuildTimeFrame(tabview.tab(TAB_VIEW_NAME1), self.fonts)
        self.build_time_frame.grid(row=2, column=0, padx=10, pady=(10,10), sticky="nsew")

        self.create_job_frame = CreateJobFrame(tabview.tab(TAB_VIEW_NAME1), self.fonts,
                                               self.input_job_frame, self.build_day_frame, self.build_time_frame)
        self.create_job_frame.grid(row=3, column=0, padx=10, pady=(10,10), sticky="nsew")

        # タブビュー(Edit job)
        self.input_job_frame = InputJobFrame(tabview.tab(TAB_VIEW_NAME2), self.fonts)
        self.input_job_frame.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsew")

        # タブビュー(Create AutoSim job)
        # T.B.D.
        # タブビュー(Coonfig)
        self.config_frame = ConfigFrame(tabview.tab(TAB_VIEW_NAME4), self.fonts)
        self.config_frame.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nsew")


class InputJobFrame(customtkinter.CTkFrame):

    def __init__(self, master, font):
        super().__init__(master)

        # テキストボックス(job名)
        self.job_name = customtkinter.CTkEntry(master=self, placeholder_text="job名", width=900, font=font)
        self.job_name.grid(row=0, column=0, padx=10, pady=(10,10), sticky="ew")

        # テキストボックス(job概要)
        self.job_desc = customtkinter.CTkEntry(master=self, placeholder_text="job概要", width=900, font=font)
        self.job_desc.grid(row=1, column=0, padx=10, pady=(10,10), sticky="ew")

        # テキストボックス(Git URL)
        self.git_url = customtkinter.CTkEntry(master=self, placeholder_text="Git URL", width=900, font=font)
        self.git_url.grid(row=2, column=0, padx=10, pady=(10,10), sticky="ew")

       # テキストボックス(Git branch)
        self.git_branch = customtkinter.CTkEntry(master=self, placeholder_text="Git対象ブランチ", width=900, font=font)
        self.git_branch.grid(row=3, column=0, padx=10, pady=(10,10), sticky="ew")

       # テキストボックス(Teams URL)
        self.teams_url = customtkinter.CTkEntry(master=self, placeholder_text="Teams URL", width=900, font=font)
        self.teams_url.grid(row=4, column=0, padx=10, pady=(10,10), sticky="ew")

       # テキストボックス(対象フォルダ)
        self.target_folder = customtkinter.CTkEntry(master=self, placeholder_text="ビルド対象フォルダ(ex. rtl/xxx)", width=900, font=font)
        self.target_folder.grid(row=5, column=0, padx=10, pady=(10,10), sticky="ew")


class BuildDayFrame(customtkinter.CTkFrame):

    def __init__(self, master, font):
        super().__init__(master)

        # ラベル(曜日選択)
        self.label_day = customtkinter.CTkLabel(master=self, text="ビルド実行曜日", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label_day.grid(row=1, column=1, padx=(20, 40), pady=(10, 10), sticky="ew")

        # チェックボックス
        self.button_sun = customtkinter.CTkCheckBox(master=self, text="Sun",
                                                    checkbox_height=25,
                                                    checkbox_width=25,
                                                    font=font,
                                                    corner_radius=50)
        self.button_mon = customtkinter.CTkCheckBox(master=self, text="Mon",
                                                    checkbox_height=25,
                                                    checkbox_width=25,
                                                    font=font,
                                                    corner_radius=50)
        self.button_tue = customtkinter.CTkCheckBox(master=self, text="Tue",
                                                    checkbox_height=25,
                                                    checkbox_width=25,
                                                    font=font,
                                                    corner_radius=50)
        self.button_wed = customtkinter.CTkCheckBox(master=self, text="Wed",
                                                    checkbox_height=25,
                                                    checkbox_width=25,
                                                    font=font,
                                                    corner_radius=50)
        self.button_thu = customtkinter.CTkCheckBox(master=self, text="Thu",
                                                    checkbox_height=25,
                                                    checkbox_width=25,
                                                    font=font,
                                                    corner_radius=50)
        self.button_fri = customtkinter.CTkCheckBox(master=self, text="Fri",
                                                    checkbox_height=25,
                                                    checkbox_width=25,
                                                    font=font,
                                                    corner_radius=50)
        self.button_sat = customtkinter.CTkCheckBox(master=self, text="Sat",
                                                    checkbox_height=25,
                                                    checkbox_width=25,
                                                    font=font,
                                                    corner_radius=50)

        self.button_sun.grid(row=1, column=2, padx=(10, 0), pady=(10, 10), sticky="ew")
        self.button_mon.grid(row=1, column=3, padx=(10, 0), pady=(10, 10), sticky="ew")
        self.button_tue.grid(row=1, column=4, padx=(10, 0), pady=(10, 10), sticky="ew")
        self.button_wed.grid(row=1, column=5, padx=(10, 0), pady=(10, 10), sticky="ew")
        self.button_thu.grid(row=1, column=6, padx=(10, 0), pady=(10, 10), sticky="ew")
        self.button_fri.grid(row=1, column=7, padx=(10, 0), pady=(10, 10), sticky="ew")
        self.button_sat.grid(row=1, column=8, padx=(10, 0), pady=(10, 10), sticky="ew")


class BuildTimeFrame(customtkinter.CTkFrame):

    def __init__(self, master, font):
        super().__init__(master)

        # ラベル(時間選択)
        self.label_time = customtkinter.CTkLabel(master=self, text="ビルド開始時間", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label_time.grid(row=0, column=1, padx=(20, 40), pady=(10, 10), sticky="ew")

        # スライドバー&ラベル
        self.var = customtkinter.IntVar()
        self.bar_time = customtkinter.CTkSlider(master=self, from_=0, to=23, width=750, height=25, variable=self.var,
                                                progress_color="DodgerBlue4", button_color="DodgerBlue3")
        self.bar_time.grid(row=0, column=2, pady=(10, 5), padx=10, sticky="ew")
        self.bar_time.set(0)
        self.label_bar_time = customtkinter.CTkLabel(master=self, textvariable=self.var, font=font)
        self.label_bar_time.grid(row=1, column=2, pady=(5, 5), padx=10, sticky="ew")


class CreateJobFrame(customtkinter.CTkFrame):

    def __init__(self, master, font, input_job_frame, build_day_frame, build_time_frame):
        super().__init__(master)

        self.input_job_frame = input_job_frame
        self.build_day_frame = build_day_frame
        self.build_time_frame = build_time_frame
        self.font = font

        self.jenkins = my_jenkins.MyJenkins()

        # ボタン(job生成)
        self.botton_job = customtkinter.CTkButton(master=self, text="job作成", font=font, height=40, width=900,
                                                  fg_color="DodgerBlue3" ,command=self.create_job_callback)
        self.botton_job.grid(row=0, column=0, padx=(20, 40), pady=(5, 10), sticky="ew")

    def create_job_callback(self):
        job_name = self.input_job_frame.job_name.get()
        job_desc = self.input_job_frame.job_desc.get()
        git_url  = self.input_job_frame.git_url.get()
        git_branch = self.input_job_frame.git_branch.get()
        teams_url = self.input_job_frame.teams_url.get()
        target_folder = self.input_job_frame.target_folder.get()
        is_sun = self.build_day_frame.button_sun.get()
        is_mon = self.build_day_frame.button_mon.get()
        is_tue = self.build_day_frame.button_tue.get()
        is_wed = self.build_day_frame.button_wed.get()
        is_thu = self.build_day_frame.button_thu.get()
        is_fri = self.build_day_frame.button_fri.get()
        is_sat = self.build_day_frame.button_sat.get()
        build_time = str(round(self.build_time_frame.bar_time.get()))

        weekday = [is_sun, is_mon, is_tue, is_wed, is_thu, is_fri, is_sat]

        if not job_name or not job_desc or not git_url or not git_branch or not teams_url:
            text = "パラメータを入力してください"
        else:
            result = self.jenkins.create(job_name, job_desc, git_url, git_branch,
                                         teams_url, target_folder, weekday, build_time)

            text = "job作成完了" if result is True else "job作成失敗"

        self.toplevel_window = None
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window =  self.toplevel_window = ToplevelWindow(self, text, self.font)
        else:
            self.toplevel_window.focus()

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, master, result, font):
        super().__init__(master)

        self.geometry("200x100+400+300")

        self.label = customtkinter.CTkLabel(self, text=result, font=font)
        self.label.pack(padx=20, pady=30)


class ConfigFrame(customtkinter.CTkFrame):

    def __init__(self, master, font):
        super().__init__(master)

        # テキストボックス(configファイル)
        self.config_file = customtkinter.CTkEntry(master=self, placeholder_text="config file", width=900, font=font)
        self.config_file.grid(row=0, column=0, padx=10, pady=(10,10), sticky="ew")

class JobLookFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, font, **kwargs):
        super().__init__(master, **kwargs)

        self.jenkins = my_jenkins.MyJenkins()

        jobs = self.jenkins.get_all_job()

        for job in jobs:
            customtkinter.CTkLabel(master=self, text=job.get('name'), font=font).grid(pady=10, sticky="w")
