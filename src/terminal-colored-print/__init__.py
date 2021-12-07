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

def colored_print(text = "", color = "White", format = None, is_bright = False):
    """
    Emulates a Python print with additional colors\n
    ``text`` the string you want to print\n
    ``color`` a string that can be [Black, Red, Green, Yellow, Blue, Magenta, Cyan, White]\n
    ``format`` a string that can be [Bold, Underline]\n
    ``is_bright`` a boolean that can be [True, False]
    """
    # Type checking the user input
    if (not isinstance(text, str)):
        colored_print("You inserted an invalid argument for 'text' in colored_print", 
            color="Red", is_bright=True, format="Bold")
    if (not isinstance(is_bright, bool)):
        colored_print("You inserted an invalid argument for 'is_bright' in colored_print", 
            color="Red", is_bright=True, format="Bold")
    try:
        if (color != None): colors[color]
        if (format != None): formats[format]
    except (KeyError):
        colored_print("You inserted an invalid key for 'color' or 'format' arguments in colored_print", 
            color="Red", is_bright=True, format="Bold")
        return
    
    #If no color has being selected, just use the default one
    result = text
    #If color is a valid key and different from None then 
    if (color != None): result = colors[color] + text + reset_code
    if (format != None): result = formats[format] + result + reset_code
    if (is_bright and color != None): result = colors[color].replace("m", ";1m") + result + reset_code
    print(result)

def colored_sprint(text = "", color = "White", format = None, is_bright = False):
    """
    Returns a decorated text\n
    ``text`` the string you want to decorate\n
    ``color`` a string that can be [Black, Red, Green, Yellow, Blue, Magenta, Cyan, White]\n
    ``format`` a string that can be [Bold, Underline]\n
    ``is_bright`` a boolean that can be [True, False]
    """
    # Type checking the user input
    if (not isinstance(text, str)):
        colored_print("You inserted an invalid argument for 'text' in colored_sprint", 
            color="Red", is_bright=True, format="Bold")
    if (not isinstance(is_bright, bool)):
        colored_print("You inserted an invalid argument for 'is_bright' in colored_sprint", 
            color="Red", is_bright=True, format="Bold")
    try:
        if (color != None): colors[color]
        if (format != None): formats[format]
    except (KeyError):
        colored_print("You inserted an invalid key for color or format arguments in colored_sprint", 
            color="Red", is_bright=True, format="Bold")
        return
    
    #If no color has being selected, just use the default one
    result = text
    #If color is a valid key and different from None then 
    if (color != None): result = colors[color] + text + reset_code
    if (format != None): result = formats[format] + result + reset_code
    if (is_bright and color != None): result = colors[color].replace("m", ";1m") + result + reset_code
    return result