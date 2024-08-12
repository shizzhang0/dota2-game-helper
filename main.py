import logging
import tkinter as tk
from tkinter import ttk, messagebox
from config import save_config, global_config
from gsi import gsi_server
from common.constants import GAME_MODE_QUICK, GAME_MODE_NORMAL
from common import utils

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log = logging.getLogger(__name__)


def add_radio_group(parent, row_index, label_text, options, string_var):
    label = ttk.Label(parent, text=label_text)
    label.grid(row=row_index, column=0, sticky=tk.EW, pady=5)
    for i, (text, value) in enumerate(options):
        radio_button = ttk.Radiobutton(parent, text=text, value=value, variable=string_var)
        radio_button.grid(row=row_index, column=i + 1, sticky=tk.EW, pady=5)


def add_checkbox_group(parent, row_index, label_text, options, int_vars):
    label = ttk.Label(parent, text=label_text)
    label.grid(row=row_index, column=0, sticky=tk.EW, pady=5)
    group_frame = ttk.Frame(parent)
    group_frame.grid(row=row_index, column=1, columnspan=2, sticky=tk.EW, pady=5)

    options_len = len(options)
    for i, text in enumerate(options):
        check_button = ttk.Checkbutton(group_frame, text=text, variable=int_vars[i])
        if options_len <= 3:
            check_button.grid(row=row_index, column=i, sticky=tk.EW)
        else:
            row_j = int(i / 3)
            col_j = row_j * 3
            check_button.grid(row=row_index + row_j, column=i + 1 - col_j, sticky=tk.EW)


def add_number_input(parent, row_index, label_text, int_var):
    def validate_input(event):
        if not (event.char.isdigit() or event.char == '\b' or event.char == ''):
            messagebox.showwarning("警告", "请输入数字！")
            return "break"

    label = ttk.Label(parent, text=label_text)
    label.grid(row=row_index, column=0, sticky=tk.EW, pady=5)
    entry = ttk.Entry(parent, textvariable=int_var)
    entry.grid(row=row_index, column=1, sticky=tk.EW, pady=5)
    entry.bind("<Key>", validate_input)


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("dota2-game-helper")
        self.create_window(480, 500)

        self.config = {}
        self.init_config()

        self.iconbitmap(utils.get_icon_file())
        self.create_widget()

    def init_config(self):
        self.config['mode'] = tk.StringVar(value=global_config.mode)
        self.config['mode'].trace_add('write', self.callback_mode)

        self.config['stack_active'] = tk.IntVar(value=int(global_config.stack_active))
        self.config['stack_active'].trace_add('write', self.callback_stack_active)
        self.config['stack_delay'] = tk.IntVar(value=global_config.stack_delay)
        self.config['stack_delay'].trace_add('write', self.callback_stack_delay)

        self.config['mid_runes_active'] = tk.IntVar(value=int(global_config.mid_runes_active))
        self.config['mid_runes_active'].trace_add('write', self.callback_mid_runes_active)
        self.config['mid_runes_delay'] = tk.IntVar(value=global_config.mid_runes_delay)
        self.config['mid_runes_delay'].trace_add('write', self.callback_mid_runes_delay)

        self.config['bounty_runes_active'] = tk.IntVar(value=int(global_config.bounty_runes_active))
        self.config['bounty_runes_active'].trace_add('write', self.callback_bounty_runes_active)
        self.config['bounty_runes_delay'] = tk.IntVar(value=global_config.bounty_runes_delay)
        self.config['bounty_runes_delay'].trace_add('write', self.callback_bounty_runes_delay)

        self.config['wisdom_runes_active'] = tk.IntVar(value=int(global_config.wisdom_runes_active))
        self.config['wisdom_runes_active'].trace_add('write', self.callback_wisdom_runes_active)
        self.config['wisdom_runes_delay'] = tk.IntVar(value=global_config.wisdom_runes_delay)
        self.config['wisdom_runes_delay'].trace_add('write', self.callback_wisdom_runes_delay)

        self.config['lotus_active'] = tk.IntVar(value=int(global_config.lotus_active))
        self.config['lotus_active'].trace_add('write', self.callback_lotus_active)
        self.config['lotus_delay'] = tk.IntVar(value=global_config.lotus_delay)
        self.config['lotus_delay'].trace_add('write', self.callback_lotus_delay)

        self.config['neutral_items_active'] = []
        item_len = len(global_config.neutral_items_active)
        for i in range(item_len):
            self.config[f'neutral_item_{i}_active'] = tk.IntVar(value=int(global_config.neutral_items_active[i]))
            self.config[f'neutral_item_{i}_active'].trace_add('write', self.callback_neutral_items_active)
            self.config['neutral_items_active'].append(self.config[f'neutral_item_{i}_active'])

        self.config['daytime_active'] = tk.IntVar(value=int(global_config.daytime_active))
        self.config['daytime_active'].trace_add('write', self.callback_daytime_active)
        self.config['roshan_active'] = tk.IntVar(value=int(global_config.roshan_active))
        self.config['roshan_active'].trace_add('write', self.callback_roshan_active)
        self.config['first_tormentor_active'] = tk.IntVar(value=int(global_config.first_tormentor_active))
        self.config['first_tormentor_active'].trace_add('write', self.callback_first_tormentor_active)
        self.config['shard_active'] = tk.IntVar(value=int(global_config.shard_active))
        self.config['shard_active'].trace_add('write', self.callback_shard_active)
        self.config['ward_purchase_active'] = tk.IntVar(value=int(global_config.ward_purchase_active))
        self.config['ward_purchase_active'].trace_add('write', self.callback_ward_purchase_active)

    def create_window(self, width, height):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 3)
        self.geometry(size)
        self.wm_minsize(width=width, height=height)
        self.wm_maxsize(width=width, height=height)

    def create_widget(self):
        left_frame = tk.Frame(self)
        right_frame = tk.Frame(self)
        bottom_frame = tk.Frame(self)

        left_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
        tk.Frame(self, width=1, bg='black').grid(row=0, column=1, sticky=tk.NS, pady=10)
        right_frame.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=10)
        bottom_frame.grid(row=1, column=0, columnspan=3, sticky=tk.EW)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # left
        left_top = tk.Frame(left_frame)
        left_top.grid(row=0, column=0, columnspan=3, sticky=tk.EW)
        ttk.Label(left_top, text='是否开启提醒').grid(row=0, column=1)
        left_top.grid_columnconfigure(0, weight=1)
        left_top.grid_columnconfigure(2, weight=1)

        add_radio_group(left_frame, 1, '游戏模式：', [('普通模式', GAME_MODE_NORMAL), ('快速模式', GAME_MODE_QUICK)],
                        self.config['mode'])
        add_radio_group(left_frame, 2, '堆野：', [('是', 1), ('否', 0)], self.config['stack_active'])
        add_radio_group(left_frame, 3, '中路神符：', [('是', 1), ('否', 0)], self.config['mid_runes_active'])
        add_radio_group(left_frame, 4, '赏金神符：', [('是', 1), ('否', 0)], self.config['bounty_runes_active'])
        add_radio_group(left_frame, 5, '智慧神符：', [('是', 1), ('否', 0)], self.config['wisdom_runes_active'])
        add_radio_group(left_frame, 6, '莲花：', [('是', 1), ('否', 0)], self.config['lotus_active'])
        add_checkbox_group(left_frame, 7, '中立物品：', ['一级', '二级', '三级', '四级', '五级'],
                           self.config['neutral_items_active'])
        add_radio_group(left_frame, 8, '白天/黑夜：', [('是', 1), ('否', 0)], self.config['daytime_active'])
        add_radio_group(left_frame, 9, '肉山：', [('是', 1), ('否', 0)], self.config['roshan_active'])
        add_radio_group(left_frame, 10, '魔方(first)：', [('是', 1), ('否', 0)], self.config['first_tormentor_active'])
        add_radio_group(left_frame, 11, '魔晶：', [('是', 1), ('否', 0)], self.config['shard_active'])
        add_radio_group(left_frame, 12, '侦察守卫：', [('是', 1), ('否', 0)], self.config['ward_purchase_active'])

        # right
        right_top = tk.Frame(right_frame)
        right_top.grid(row=0, column=0, columnspan=2, sticky=tk.EW)
        ttk.Label(right_top, text='提前提醒时间(单位：秒)').grid(row=0, column=1)
        right_top.grid_columnconfigure(0, weight=1)
        right_top.grid_columnconfigure(2, weight=1)

        add_number_input(right_frame, 1, '堆野', self.config['stack_delay'])
        add_number_input(right_frame, 2, '中路神符', self.config['mid_runes_delay'])
        add_number_input(right_frame, 3, '赏金神符', self.config['bounty_runes_delay'])
        add_number_input(right_frame, 4, '智慧神符', self.config['wisdom_runes_delay'])
        add_number_input(right_frame, 5, '莲花', self.config['lotus_delay'])

        tk.Frame(right_frame, height=1, bg='black').grid(row=6, column=0, columnspan=3, sticky=tk.EW, pady=10)

        text_widget = tk.Text(right_frame, wrap=tk.CHAR, height=7, width=30)
        text_widget.insert(tk.END,
                           '''需要找到游戏安装目录下的steamapps\common\dota 2 beta\game\dota\cfg目录，在里面新建一个gamestate_integration文件夹，然后将cfg文件复制进去\n也可以点击下面按钮自动复制进去''')
        text_widget.config(state=tk.DISABLED)
        text_widget.grid(row=7, column=0, columnspan=3, pady=5)

        ttk.Button(right_frame, text='自动复制', command=self.on_btn_copy).grid(row=8, column=0, columnspan=3,
                                                                                sticky=tk.EW, pady=5)

        # bottom
        ttk.Button(bottom_frame, text='保存', command=self.on_btn_save).grid(row=0, column=1)
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(2, weight=1)

    def callback_mode(self, *args):
        global_config.mode = self.config['mode'].get()

    def callback_stack_active(self, *args):
        global_config.stack_active = bool(self.config['stack_active'].get())

    def callback_stack_delay(self, *args):
        global_config.stack_delay = self.config['stack_delay'].get()

    def callback_mid_runes_active(self, *args):
        global_config.mid_runes_active = bool(self.config['mid_runes_active'].get())

    def callback_mid_runes_delay(self, *args):
        global_config.mid_runes_delay = self.config['mid_runes_delay'].get()

    def callback_bounty_runes_active(self, *args):
        global_config.bounty_runes_active = bool(self.config['bounty_runes_active'].get())

    def callback_bounty_runes_delay(self, *args):
        global_config.bounty_runes_delay = self.config['bounty_runes_delay'].get()

    def callback_wisdom_runes_active(self, *args):
        global_config.wisdom_runes_active = bool(self.config['wisdom_runes_active'].get())

    def callback_wisdom_runes_delay(self, *args):
        global_config.wisdom_runes_delay = self.config['wisdom_runes_delay'].get()

    def callback_lotus_active(self, *args):
        global_config.lotus_active = bool(self.config['lotus_active'].get())

    def callback_lotus_delay(self, *args):
        global_config.lotus_delay = self.config['lotus_delay'].get()

    def callback_neutral_items_active(self, *args):
        for i, int_var in enumerate(self.config['neutral_items_active']):
            global_config.neutral_items_active[i] = bool(int_var.get())

    def callback_daytime_active(self, *args):
        global_config.daytime_active = bool(self.config['daytime_active'].get())

    def callback_roshan_active(self, *args):
        global_config.roshan_active = bool(self.config['roshan_active'].get())

    def callback_first_tormentor_active(self, *args):
        global_config.first_tormentor_active = bool(self.config['first_tormentor_active'].get())

    def callback_shard_active(self, *args):
        global_config.shard_active = bool(self.config['shard_active'].get())

    def callback_ward_purchase_active(self, *args):
        global_config.ward_purchase_active = bool(self.config['ward_purchase_active'].get())

    @staticmethod
    def on_btn_save():
        try:
            save_config(global_config)
        except Exception as error:
            log.error(f"fail to save config : {error}")
            messagebox.showerror('错误', '保存失败，请删除config.json后重新打开程序')
            return
        messagebox.showinfo('信息', '保存成功!')

    @staticmethod
    def on_btn_copy():
        try:
            utils.write_gsi_file()
        except Exception as error:
            log.error(f"fail to write cfg file : {error}")
            messagebox.showerror('错误', '复制失败请手动操作!')
            return
        messagebox.showinfo('信息', '复制成功!')


if __name__ == '__main__':
    gsi_server.run()
    app = App()
    app.mainloop()
