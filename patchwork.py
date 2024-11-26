from graphix import Window, Point, Rectangle, Circle
from graphix_plus import full_fill

def get_params():
    #Allowed inputs
    valid_sizes = [5, 7, 9]
    valid_colours = ["red", "green", "blue", "magenta", "orange", "purple"]
    
    while True:
        #Patchwork Params
        patchwork_size = int(input("What patchwork size do you want? "))
        if patchwork_size not in valid_sizes:
            print(f"(-) Patchwork size must be one of {valid_sizes}.\n")
            continue
        
        #Colour Params
        colours = []
        colours.append(input("Enter first colour: "))
        colours.append(input("Enter second colour: "))
        colours.append(input("Enter third colour: "))
        if len(colours) != len(set(colours)):
            print("(-) All colours must be different.\n")
            continue
        if (colours[0] not in valid_colours) or (colours[1] not in valid_colours) or (colours[2] not in valid_colours):
            print(f"(-) Colours must be one of {valid_colours}.\n")
            continue
        break
    
    return patchwork_size*100, colours

def pen_patch():
    ...

def fin_patch():
    ...
    
def pln_patch():
    ...

def main():
    #Program Constants
    PATCH_SIZE = 100
    PATCHWORK_SIZE, COLOURS = get_params()
    
    #Set up window
    win = Window("Patchwork", PATCHWORK_SIZE, PATCHWORK_SIZE)
    win.background_colour = "white"
    
    #Close window after mouse click
    win.get_mouse()
    win.close()
    
main()