from sys import argv
import argparse
from pathlib import Path
import os
import yaml
from Stiledprint import stlprint
from pprint import pprint

PATH = "/home/" + os.getlogin() + "/.config/alacritty/"
ALACRITTY_FILE_PATH = PATH + "alacritty.yml"
THEME_FILE_PATH = PATH + "pytheme/themes/themes/"
FONT_FILE_PATH = PATH + "pytheme/themes/fonts"

def changecursor():
    try: 
        argtheme = cli()
        
        with open(ALACRITTY_FILE_PATH , "r") as alacritty_file:
            alacritty = yaml.load(alacritty_file, Loader=yaml.FullLoader)
        
        alacritty["cursor"]["style"]["shape"] = argtheme.cursor[0]
        if argtheme.cursor[1] != None:
            a = None
            if argtheme.cursor[1] == "0":
                a = "Off"
            else:
                a = "On"
            alacritty["cursor"]["style"]["blinking"] = a
        if argtheme.cursor[2] != None:
            alacritty["cursor"]["style"]["blink-interval"] = int(argtheme.cursor[2]) 
        with open(ALACRITTY_FILE_PATH, "w") as f:
            yaml.dump(alacritty, f)
    

    except yaml.YAMLError or FileNotFoundError as e:
        excepterYaml(e)
def changepadding():
    try: 
        argtheme = cli()
        
        with open(ALACRITTY_FILE_PATH , "r") as alacritty_file:
            alacritty = yaml.load(alacritty_file, Loader=yaml.FullLoader)
        
       

        
        alacritty["window"]["padding"]["x"] = argtheme.padding[0]
        alacritty["window"]["padding"]["y"] = argtheme.padding[1]

        with open(ALACRITTY_FILE_PATH, "w") as f:
            yaml.dump(alacritty, f)
    

    except yaml.YAMLError or FileNotFoundError as e:
        excepterYaml(e)

def changesize():
    try: 
        argtheme = cli()
        
        with open(ALACRITTY_FILE_PATH , "r") as alacritty_file:
            alacritty = yaml.load(alacritty_file, Loader=yaml.FullLoader)
            
        alacritty["font"]["size"] = float(argtheme.size)

        with open(ALACRITTY_FILE_PATH, "w") as f:
            yaml.dump(alacritty, f)
    

    except yaml.YAMLError or FileNotFoundError as e:
        excepterYaml(e)


def changeopacity():
    try: 
        argtheme = cli()
        
        with open(ALACRITTY_FILE_PATH , "r") as alacritty_file:
            alacritty = yaml.load(alacritty_file, Loader=yaml.FullLoader)
            
        alacritty["window"]["opacity"] = float(argtheme.opacity)

        with open(ALACRITTY_FILE_PATH, "w") as f:
            yaml.dump(alacritty, f)
    

    except yaml.YAMLError or FileNotFoundError as e:
        excepterYaml(e)

def changefont():
    try: 
        argtheme = cli()
        
        with open(FONT_FILE_PATH + ".yaml", "r") as fonts_file:
            fonts = yaml.load(fonts_file, Loader=yaml.FullLoader)
        with open(ALACRITTY_FILE_PATH , "r") as alacritty_file:
            alacritty = yaml.load(alacritty_file, Loader=yaml.FullLoader)
        
        alacritty["font"]["normal"]["family"] = fonts["fonts"][argtheme.font]
  
        with open(ALACRITTY_FILE_PATH, "w") as f:
            yaml.dump(alacritty, f)
        
        return True

    except yaml.YAMLError or FileNotFoundError as e:
        excepterYaml(e)

def changetheme():
    argtheme = cli()
    if argtheme.theme == "ls":
        
        pprint(os.listdir(THEME_FILE_PATH))
    else:
        try:
            argtheme = cli()

            with open(THEME_FILE_PATH + argtheme.theme + ".yaml", "r") as theme_file:
                theme = yaml.load(theme_file, Loader=yaml.FullLoader)
            with open(ALACRITTY_FILE_PATH , "r") as alacritty_file:
                alacritty = yaml.load(alacritty_file, Loader=yaml.FullLoader)

            if "colors" not in theme:
                print(f"Theme {theme_file} has not colors configuration")
                return False
            alacritty["colors"] = theme["colors"]

            with open(ALACRITTY_FILE_PATH, "w") as f:
                yaml.dump(alacritty, f)
            
            return True
        except yaml.YAMLError or FileNotFoundError as e:
            excepterYaml(e)

def excepterYaml(e):
    if e == FileNotFoundError:
        print("Error al encontrar el archivo")
    if e == yaml.YAMLError:
        print(("Yaml error at parsing file, at line {0.problem_mark.line}, "
              "at column {0.problem_mark.column}:\n {0.problem} {0.context} \n").format(e))


def cli():
    parser = argparse.ArgumentParser(
        prog="pytheme",
        description="pytheme command implementation for your terminal"
    )
    parser.add_argument("-o", "--opacity", help="changes your terminal opacity")#, "OPACITY")
    parser.add_argument("-t", "--theme", help="changes your terminal theme") #, "THEME")
    parser.add_argument("-f", "--font", help="changes your terminal font") #, "FONT")
    parser.add_argument("-s", "--size", help="changes your terminal size font") #, "SIZE")
    parser.add_argument("-p", "--padding", type=int, nargs="+", help="changes your terminal padding") #, "padding")
    parser.add_argument("-c", "--cursor", type=str ,nargs="+",help="changes your terminal cursor")

    
    return parser.parse_args()




def main():
    args = cli()
    #print(f"theme es igual a {args.theme}")
    if args.theme != None:
        changetheme()
    if args.font != None:
        changefont()
    if args.opacity != None:
        changeopacity()
    if args.size != None:
        changesize()
    if args.padding != None:
        changepadding()
    if args.cursor != None:
        changecursor()
if __name__ == "__main__":
    main()