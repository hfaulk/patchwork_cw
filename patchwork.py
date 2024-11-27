from graphix import Window, Point, Rectangle, Circle
from graphix_plus import full_fill, draw_rect, draw_circ, relative_point

def get_params() -> tuple[int, list]:
    #Allowed inputs
    valid_sizes:list[int] = [5, 7, 9]
    valid_colours:list[str] = ["red", "green", "blue", "magenta", "orange", "purple"]
    
    while True:
        #Patchwork Params
        patchwork_size:int = int(input("What patchwork size do you want? "))
        if patchwork_size not in valid_sizes:
            print(f"(-) Patchwork size must be one of {valid_sizes}.\n")
            continue
        
        #Colour Params
        colours:list[str] = []
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

def pen_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str) -> None:
    sub_patch_size:int = patch_size // 5
    patch_flag:bool = True
    true_count:int = 0
    false_count:int = 0
    for y in range(top_left_y, top_left_y + patch_size, sub_patch_size):
        for x in range(top_left_x, top_left_x + patch_size, sub_patch_size):
            draw_rect(window, Point(x, y), Point(x+sub_patch_size, y+sub_patch_size), "white", "black")
                        
            if patch_flag == True and true_count < 1:
                flipped = False
                true_count += 1
            elif patch_flag == False and false_count < 1:
                flipped = False
                false_count += 1
            elif patch_flag == True and true_count == 1:
                flipped = True
                true_count = 0
            elif patch_flag == False and false_count == 1:
                flipped = True
                false_count = 0
            sub_pen_patch(window, x, y, sub_patch_size, colour, patch_flag, flipped)
            
            patch_flag:bool = not patch_flag
    
def sub_pen_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str, variant:bool, flipped:bool) -> None:
    rect_size:int = patch_size // 4 #There are 4 rectangles per patch
    patch_flag:bool = True
    
    colours = [colour, "white"]
    
    if flipped == True: colours = reverse_list(colours)
        
    if variant == True:
        for y in range(top_left_y, top_left_y + patch_size, rect_size):
            if patch_flag == True: fill_colour = colours[0]
            elif patch_flag == False: fill_colour = colours[1]
            patch_flag:bool = not patch_flag
            draw_rect(window, Point(top_left_x, y), Point(top_left_x + patch_size, y+rect_size), fill_colour, "black")
    elif variant == False:
        for x in range(top_left_x, top_left_x + patch_size, rect_size):
            if patch_flag == True: fill_colour = colours[0]
            elif patch_flag == False: fill_colour = colours[1]
            patch_flag:bool = not patch_flag
            draw_rect(window, Point(x, top_left_y), Point(x + rect_size, top_left_y + patch_size), fill_colour, "black")

def fin_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str) -> None:
    ...
    
def pln_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str) -> None:
    draw_rect(window, Point(top_left_x, top_left_y), Point(top_left_x + patch_size, top_left_y + patch_size), colour, "black")

def reverse_list(list_to_reverse:list) -> list:
    reversed_list:list = []
    for index in range(len(list_to_reverse) - 1, -1, -1):
        reversed_list.append(list_to_reverse[index])
    return reversed_list

def main():
    #Program Constants
    PATCH_SIZE:int = 100
    PATCHWORK_SIZE, COLOURS = get_params()
    
    #Set up window
    win = Window("Patchwork", PATCHWORK_SIZE, PATCHWORK_SIZE)
    win.background_colour = "white"
    
    #Testing
    pen_patch(win, 150, 230, 100, COLOURS[0])
    
    #Close window after mouse click
    win.get_mouse()
    win.close()
    
main()