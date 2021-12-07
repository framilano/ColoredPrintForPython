#Usage example
#colored_print(text="Hello!", color="Blue", is_bright=True, format="Underline")
#print(colored_sprint("Hello sprint!", "Red", format="Underline", is_bright=False))

#Available colors
colors = {
"Black": "\033[30m",
"Red": "\033[31m",
"Green": "\033[32m",
"Yellow": "\033[33m",
"Blue": "\033[34m",
"Magenta": "\033[35m",
"Cyan": "\033[36m",
"White": "\033[37m"
}

#Available formats
formats = {"Bold":'\033[1m', "Underline":'\033[4m'}

#Reset code to end the 'decoration'
reset_code = "\033[0m"

def colored_print(text, color = "Red", format = None, is_bright = False):
    """
    Emulates a Python print with additional colors\n
    ``text`` the string you want to print\n
    ``color`` a string that can be [Black, Red, Green, Yellow, Blue, Magenta, Cyan, White]\n
    ``formats`` a string that can be [Bold, Underline]\n
    ``bright`` a boolean that can be [True, False]
    """
    try:
        colors[color]
        formats[format]
    except (KeyError):
        colored_print("You inserted an invalid key for color or format arguments", color="Red", is_bright=True, format="Bold")
        return
    result = colors[color] + text + reset_code
    if (format != None): result = formats[format] + result + reset_code
    if (is_bright): result = colors[color].replace("m", ";1m") + result + reset_code
    print(result)

def colored_sprint(text, color = "Red", format = None, is_bright = False) -> str:
    """
    Returns a decorated text\n
    ``text`` the string you want to decorate\n
    ``color`` a string that can be [Black, Red, Green, Yellow, Blue, Magenta, Cyan, White]\n
    ``formats`` a string that can be [Bold, Underline]\n
    ``bright`` a boolean that can be [True, False]
    """
    try:
        colors[color]
        formats[format]
    except (KeyError):
        colored_print("You inserted an invalid key for color or format arguments", color="Red", is_bright=True, format="Bold")
        return
    result = colors[color] + text + reset_code
    if (format != None): result = formats[format] + result + reset_code
    if (is_bright): result = colors[color].replace("m", ";1m") + result + reset_code
    return result
