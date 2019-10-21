import click
import os
import json
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
import re

root = tk.Tk()
style = ttk.Style(root)
style.theme_use('clam')

_, color = askcolor((255, 255, 0), root)
os.makedirs('.vscode', exist_ok=True)

# peacock
try:
    with open(".vscode/settings.json", "r") as f:
        vsc = json.load(f)
except FileNotFoundError:
    vsc = {}
vsc["peacock.color"] = color
with open(".vscode/settings.json", "w+") as f:
    json.dump(vsc, f)

# iterm-tab-colors
tc_config = os.path.expanduser("~/.oh-my-zsh/custom/plugins/iterm-tab-color/.tc-config")
cmd = "sed -i.bak '/%s*/d' %s"%(os.getcwd().replace('/', '\/'), tc_config)
os.system(cmd)
with open(tc_config, "a+") as f:
    f.write(f"{os.getcwd()}*={color}\n")
