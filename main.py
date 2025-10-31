import json
import os

colors = {
    "terminal.background": "bg",
    "terminal.foreground": "fg",
    "terminal.ansiRed": "red",
    "terminal.ansiGreen": "green",
    "terminal.ansiBlue": "blue",
    "terminal.ansiBlack": "black",
    "terminal.ansiWhite": "white",
    "terminal.ansiMagenta": "magenta",
    "terminal.ansiCyan": "cyan",
    "terminal.ansiYellow": "yellow",
    "terminal.ansiBrightRed": "bright-red",
    "terminal.ansiBrightGreen": "bright-green",
    "terminal.ansiBrightBlue": "bright-blue",
    "terminal.ansiBrightBlack": "bright-black",
    "terminal.ansiBrightWhite": "bright-white",
    "terminal.ansiBrightCyan": "bright-cyan",
    "terminal.ansiBrightMagenta": "bright-magenta",
    "terminal.ansiBrightYellow": "bright-yellow",
}

for file in os.listdir("./vscode"):
    text = ":root {\n"
    with open(f"./vscode/{file}") as f:
        dictionary = json.load(f)
        for key in colors.keys():
            color = dictionary["workbench.colorCustomizations"][key]
            text += f"	--{colors[key]}: {color};\n"
    text += "}"
    file_name = file.split(".")[0]
    file_name_words = file_name.split(" ")
    file_name_new = file_name_words.pop(0).lower()
    for word in file_name_words:
        file_name_new += word.capitalize()
    file_name_new = file_name_new.replace("(", "").replace(")", "")
    output_file = f"./output/{file_name_new}.css"
    print(output_file)
    with open(output_file, "w") as out:
        out.write(text)
