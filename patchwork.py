from graphix import Window, Point
from graphix_plus import draw_rect, draw_line
from time import sleep

def get_params() -> tuple[int, list]:
    #Allowed inputs
    valid_sizes:list[int] = [5, 7, 9]
    valid_colours:list[str] = ["red", "green", "blue", "magenta", "orange", "purple"]
    
    while True:
        #Patchwork Params
        patchwork_size:int = input("What patchwork size do you want? ")
        if not patchwork_size.isdigit():
            print("(-) Patchwork size must be an integer\n")
            continue
        else: patchwork_size = int(patchwork_size)
        if patchwork_size not in valid_sizes:
            print(f"(-) Patchwork size must be one of {valid_sizes}.\n")
            continue
        
        #Colour Params
        colours:list[str] = []
        colours.append(input("Enter first colour: ").lower())
        colours.append(input("Enter second colour: ").lower())
        colours.append(input("Enter third colour: ").lower())
        if (colours[0] not in valid_colours) or (colours[1] not in valid_colours) or (colours[2] not in valid_colours):
            print(f"(-) Colours must be one of {valid_colours}.\n")
            continue
        if len(colours) != len(set(colours)):
            print("(-) All colours must be different.\n")
            continue
        break
    
    return patchwork_size*100, colours

def pen_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str) -> list:
    sub_patch_size:int = patch_size // 5
    patch_flag:bool = True
    true_count, false_count = 0,0
    patch_components:list = []
    for y in range(top_left_y, top_left_y + patch_size, sub_patch_size):
        for x in range(top_left_x, top_left_x + patch_size, sub_patch_size):
            patch_components.append(draw_rect(window, Point(x, y), Point(x+sub_patch_size, y+sub_patch_size), "white", "black"))
            
            if patch_flag and true_count < 1:
                flipped:bool = False
                true_count += 1
            elif not patch_flag and false_count < 1:
                flipped:bool = False
                false_count += 1
            elif patch_flag and true_count == 1:
                flipped:bool = True
                true_count = 0
            elif not patch_flag and false_count == 1:
                flipped:bool = True
                false_count = 0
                
            patch_components += sub_pen_patch(window, x, y, sub_patch_size, colour, patch_flag, flipped)
            patch_flag:bool = not patch_flag
    return patch_components
    
def sub_pen_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str, variant:bool, flipped:bool) -> list:
    rect_size:int = patch_size // 4 #There are 4 rectangles per patch
    patch_flag:bool = True
    
    colours:list = [colour, "white"]
    
    patch_components:list = []

    if flipped: colours.reverse()
        
    if variant:
        for y in range(top_left_y, top_left_y + patch_size, rect_size):
            fill_colour = colours[int(not patch_flag)]
            patch_flag:bool = not patch_flag
            patch_components.append(draw_rect(window, Point(top_left_x, y), Point(top_left_x + patch_size, y+rect_size), fill_colour, "black"))
    elif not variant:
        for x in range(top_left_x, top_left_x + patch_size, rect_size):
            fill_colour = colours[int(not patch_flag)]
            patch_flag:bool = not patch_flag
            patch_components.append(draw_rect(window, Point(x, top_left_y), Point(x + rect_size, top_left_y + patch_size), fill_colour, "black"))
    return patch_components

def fin_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str) -> list:
    draw_rect(window, Point(top_left_x, top_left_y), Point(top_left_x + patch_size, top_left_y + patch_size), "white", "black")
    line_sep:int = patch_size // 10
    count:int = 1
    patch_components:list = []
    for x in range(top_left_x, top_left_x + patch_size, line_sep):
        point_1:Point = Point(x, top_left_y)
        point_2:Point = Point(top_left_x + patch_size, top_left_y + (count + line_sep))
        patch_components.append(draw_line(window, point_1, point_2, colour))
        count += line_sep
    count:int = 1
    for y in range(top_left_y, top_left_y + patch_size, line_sep):
        point_1:Point = Point(top_left_x, y)
        point_2:Point = Point(top_left_x + (count + line_sep), top_left_y + patch_size)
        patch_components.append(draw_line(window, point_1, point_2, colour))
        count += line_sep
    return patch_components
    
def pln_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, colour:str) -> list:
    rect = draw_rect(window, Point(top_left_x, top_left_y), Point(top_left_x + patch_size, top_left_y + patch_size), colour, "black")
    return [rect]

def patchwork(window:Window, patchwork_size:int, patch_size:int, colours:list) -> list:
    patches = []
    for x in range(0, patchwork_size, patch_size):
        patches.append([])
        for y in range(0, patchwork_size, patch_size):
            if (y == 0 and x != 0) or (x == patchwork_size - patch_size) and (y != x):
                patches[-1].append(fin_patch(window, x, y, patch_size, colours[1]))
            if ((x//patch_size) % 2 == 0):
                if (x <= y) and (x > patch_size) and (y < patchwork_size - patch_size):
                    patches[-1].append(pen_patch(window, x, y, patch_size, colours[0]))
                elif (y >= x):
                    patches[-1].append(pln_patch(window, x, y, patch_size, colours[0]))
                elif (y >= patch_size) and (x < patchwork_size - patch_size):
                    patches[-1].append(pln_patch(window, x, y, patch_size, colours[1]))
            else:
                if (y >= patch_size) and (y < patchwork_size - patch_size) and (y >= x):
                    patches[-1].append(pen_patch(window, x, y, patch_size, colours[2]))
                elif (y <= x) and (y >= patch_size):
                    patches[-1].append(pln_patch(window, x, y, patch_size, colours[1]))
                elif (y == patchwork_size - patch_size):
                    patches[-1].append(pln_patch(window, x, y, patch_size, colours[2]))
    return patches

#Challenge Functions
def round_down_nearest_hundred(to_round:int) -> int:
    if to_round < 100: hundred:int = 0
    else: hundred:str = str(to_round)[0]
    return int(hundred)

def outline_patch(window:Window, top_left_x:int, top_left_y:int, patch_size:int, outline_width:int=5) -> list:
    outline = []
    corners = [(top_left_x, top_left_y),
               (top_left_x + patch_size, top_left_y),
               (top_left_x + patch_size, top_left_y + patch_size),
               (top_left_x, top_left_y + patch_size)]
    for i in range(len(corners)):
        next_i = (i + 1) % len(corners)
        outline.append(draw_line(window, Point(corners[i][0], corners[i][1]), Point(corners[next_i][0], corners[next_i][1]), "black", outline_width = outline_width))
        
    return outline

def undraw_patch(patch_components:list) -> None:
    for component in patch_components:
        component.undraw()
        
def find_adjacent_empty_patch(all_patches:list, selected_patch_index:list[int, int], direction:str) -> list[int, int]:
    directions:dict = {"Left":  [i for i in range(selected_patch_index[0]-1, -1, -1)],
                       "Right": [i for i in range(selected_patch_index[0]+1, len(all_patches), 1)],
                       "Up":    [i for i in range(selected_patch_index[1]-1, -1, -1)],
                       "Down":  [i for i in range(selected_patch_index[1]+1, len(all_patches[selected_patch_index[0]]), 1)]}
    
    adjacent_empty:list = []
    
    if direction in ["Left", "Right"]:
        for i in directions[direction]:
            if all_patches[i][selected_patch_index[1]] == []:
                adjacent_empty.append([i, selected_patch_index[1]])
                break
    elif direction in ["Up", "Down"]:
        for i in directions[direction]:
            if all_patches[selected_patch_index[0]][i] == []:
                adjacent_empty.append([selected_patch_index[0], i])
                break
    if adjacent_empty == []: return None
    else: return adjacent_empty[0]

def coordinate_delta(original_coords:list, new_coords:list) -> list:
    delta = [(new_coords[0] - original_coords[0]),
             (new_coords[1] - original_coords[1])]
    return delta

def move_patch(window:Window, patches:list, selected_index:list[int ,int], new_index:list[int, int]) -> list:
    ANIM_STEP = 10
    #Getting list with each object that makes selected patch
    selected_patch_components = patches[selected_index[0]][selected_index[1]]
    #Getting difference in coords so can move to correct position
    delta = coordinate_delta(selected_index, new_index)
    delta = [i*100 for i in delta] #x100 to both coords to scale up to size of tiles
    if delta[0] != 0: increment = [delta[0] // ANIM_STEP, 0]
    else: increment = [0, delta[1] // ANIM_STEP]
    #Moving each part of patch then updating list of all patches
    for i in range(ANIM_STEP):
        for component in selected_patch_components:
            component.undraw() #Have to redraw with each movement to remain on top
            component.move(*increment)
            component.draw(window)
        sleep(0.01)
        
    patches[new_index[0]][new_index[1]] = patches[selected_index[0]][selected_index[1]]
    patches[selected_index[0]][selected_index[1]] = []
    
    return patches
    
def handle_click(window:Window, patch_size:int, click_pos:Point) -> dict:
    rounded_x = round_down_nearest_hundred(click_pos.x)
    rounded_y = round_down_nearest_hundred(click_pos.y)
    outline:list = outline_patch(window, rounded_x * 100, rounded_y * 100, patch_size)
    
    return {"x": rounded_x,
            "y": rounded_y,
            "outline": outline}
    
def handle_key(window:Window, patches:list, key:str, rounded_x:int, rounded_y:int, outline:list, patch_size:int, colours:list[str]):
    digit_keys:list = [str(i) for i in range(1, 10)]
    action_keys:list = ["x", "Escape", "Left", "Right", "Up", "Down"]
    
    selected_patch:list = patches[rounded_x][rounded_y]
    
    if key in digit_keys:
        return handle_digit(window, selected_patch, key, patches, rounded_x, rounded_y, outline, patch_size, colours)
    elif key in action_keys:
        return handle_action(window, selected_patch, key, patches, rounded_x, rounded_y, outline)
    
def handle_digit(window:Window, selected_patch:list, key:str, patches:list, rounded_x:int, rounded_y:int, outline:list, patch_size:int, colours:list) -> list:
    digit_keys:dict = {"1": [pen_patch, 0], "2": [pen_patch, 1], "3": [pen_patch, 2],
                       "4": [fin_patch, 0], "5": [fin_patch, 1], "6": [fin_patch, 2],
                       "7": [pln_patch, 0], "8": [pln_patch, 1], "9": [pln_patch, 2]}
    
    rounded_x *= 100
    rounded_y *= 100
    
    if selected_patch == []:
        undraw_patch(outline)
        patches[rounded_x//100][rounded_y//100] = digit_keys[key][0](window, rounded_x, rounded_y, patch_size, colours[digit_keys[key][1]])
        outline:list = outline_patch(window, rounded_x, rounded_y, patch_size)
        
    return patches, outline
    
def handle_action(window:Window, selected_patch:list, key:str, patches:list, rounded_x:int, rounded_y:int, outline:list) -> list:
    action_keys:dict = {"x": undraw_patch, "Escape": undraw_patch,
                        "Left": move_patch, "Right": move_patch, "Up": move_patch, "Down": move_patch}
    
    if key in ["Left", "Right", "Up", "Down"]:
        if selected_patch != []:
            adjacent_coords = find_adjacent_empty_patch(patches, [rounded_x, rounded_y], key)
            if adjacent_coords != None: 
                patches = action_keys[key](window, patches, [rounded_x, rounded_y], adjacent_coords)
    elif key == "x":
        if selected_patch != []:
            action_keys[key](selected_patch)
            patches[rounded_x][rounded_y] = []
    elif key == "Escape":
        action_keys[key](outline)
        
    return patches, outline

#Main
def main() -> None:
    #Program Constants
    PATCH_SIZE:int = 100
    PATCHWORK_SIZE, COLOURS = get_params()
    
    #Set up window
    win = Window("Patchwork", PATCHWORK_SIZE, PATCHWORK_SIZE)
    win.background_colour = "white"
    
    #Draw patchwork
    patches = patchwork(win, PATCHWORK_SIZE, PATCH_SIZE, COLOURS)
    active_selection:bool = False
    
    while True:
        if not active_selection:
            click = win.get_mouse()
            click_data = handle_click(win, PATCH_SIZE, click)
            active_selection = True
            
        key = win.get_key()
        if key == "Escape": active_selection = False
        patches, click_data["outline"] = handle_key(win, patches, key, click_data["x"], click_data["y"], click_data["outline"], PATCH_SIZE, COLOURS)
    
main()