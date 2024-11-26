"""
graphix_plus.py - An extension to graphix.py that adds general QoL features

This library extends the functionality of the graphix library to make it easier and more intuitive to use.

INSTALLATION:
Add to project directory along with main graphix.py library
"""

__version__ = "0.4"
__author__ = "Harry Faulkner"

#Imports
from graphix import GraphixObject, Window, Text, Point, Circle, Rectangle

#Classes
class Group:
    """
    A class that adds object grouping functionality to execute functions on multiple objects in one statement.

    Attributes
    -----
    group_id : str
        Identifier for instantiated group, blank by default

    Methods
    -----
    add(item):
        Adds parsed item/s to group. 'item' can be either single GraphixObject, or list of GraphixObjects.
    remove(item):
        Removes parsed item from group. 'item' can only be a singular GraphixObject.
    draw(window):
        Iterates over each item in group and draws to parsed window. 'window' must be graphix Window object.
    undraw():
        Iterates over each item in group and undraws from screen.
    move(dx, dy):
        Moves all objects in group by same vector.
    get_items():
        Returns list of every item in group.
    get_id():
        Returns string of 'group_id'.
    """
    def __init__(self, *, group_id:str=""):
        self.id = group_id
        self.items = []

    def add(self, item:GraphixObject | list) -> None:
        """
        Adds parsed item/s to group. 'item' can be either single GraphixObject, or list of GraphixObjects.

        Parameters
        -----
        item : GraphixObject or list
            Object or list of objects that is to be added to group

        Returns
        -----
        None

        See Also
        -----
        None
        """
        if isinstance(item, GraphixObject):
            self.items.append(item)
        elif isinstance(item, list):
            for given_item in item:
                if isinstance(given_item, GraphixObject):
                    self.items.append(given_item)
                else:
                    raise Exception(f"Provided item '{given_item}' is not of type {GraphixObject}")
        else:
            raise Exception(f"Provided item '{item}' is not one of type [{GraphixObject}, {list}]")

    def remove(self, item:GraphixObject) -> None:
        """
        Removes parsed item from group. 'item' can only be a singular GraphixObject.

        Parameters
        -----
        item : GraphixObject
            Object that is to be removed from group

        Returns
        -----
        None

        See Also
        -----
        None
        """
        self.items.remove(item)

    def draw(self, window:Window) -> None:
        """
        Iterates over each item in group and draws to parsed window. 'window' must be graphix Window object.

        Parameters
        -----
        window : Window
            Window object that the group is to be drawn onto

        Returns
        -----
        None

        See Also
        -----
        None
        """
        for item in self.items:
            item.draw(window)

    def undraw(self) -> None:
        """
        Iterates over each item in group and undraws from screen.

        Parameters
        -----
        None

        Returns
        -----
        None

        See Also
        -----
        None
        """
        for item in self.items:
            item.undraw()

    def move(self, dx:int, dy:int) -> None:
        """
        Moves all objects in group by same vector.

        Parameters
        -----
        dx : int
            Amount each object should be moved in x-direction
        dy : int
            Amount each object should be moved in y-direction

        Returns
        -----
        None

        See Also
        -----
        None
        """
        for item in self.items:
            item.move(dx, dy)

    def get_items(self) -> list:
        """
        Returns list of every item in group.

        Parameters
        -----
        None

        Returns
        -----
        List

        See Also
        -----
        None
        """
        return self.items

    def get_id(self) -> str:
        """
        Returns string of 'group_id'.

        Parameters
        -----
        None

        Returns
        -----
        String

        See Also
        -----
        None
        """
        return self.id

#General Functions
def full_fill(item: GraphixObject, fill_colour:str, outline_colour:str="") -> None:
    """
    Fills same colour for both inside and outline of given object.
    Passing None will do nothing.

    Parameters
    -----
    item : GraphixObject
        Item to colour fill
    fill_colour : str
        Colour to fill inside of shape
    outline_colour : str
        Colour to make the outline of shape (if left blank, shape will have no outline)

    Returns
    -----
    None

    See Also
    -----
    None
    """
    if fill_colour is None: pass
    else:
        if outline_colour == "": outline_colour = fill_colour
        item.fill_colour = fill_colour
        item.outline_colour = outline_colour

def relative_point(ref_item:GraphixObject, dx:int, dy:int) -> Point:
    """
    Takes centre of parsed reference object as (0,0) and gives new point dx,dy away from that centre.

    Parameters
    -----
    ref_item : GraphixObject
        Object whose centre acts as 0,0 for the new point
    dx : int
        Difference in x-direction from centre of reference object
    dy: int
        Difference in y-direction from centre of reference object

    Returns
    -----
    Point

    See Also
    -----
    None
    """
    ref_centre = ref_item.get_centre()
    new_x = ref_centre.x + dx
    new_y = ref_centre.y + dy
    new_point = Point(new_x, new_y)

    return new_point

def draw_rect(window:Window,
              top_left_point:Point,
              bottom_right_point:Point,
              fill_colour:str,
              outline_colour:str="",
              *,
              outline_width:int=1):
    """
    Draws a rectangle on a given window at the given location.

    Parameters
    -----
    window : Window
        Window to draw rectangle into
    top_left_point : Point
        Top left point of rectangle
    bottom_right_point : Point
        Bottom right point of rectangle
    fill_colour : str
        Colour to fill inside rectangle
    outline_colour : str, optional
        Colour to make the outline of rectangle (if left blank, rectangle will have no outline)
    outline_width : int, optional
        Determines width of shape's outline (default value of 0.5)
        
    Returns
    -----
    None
    
    See Also
    -----
    full_fill()
    """
    rect = Rectangle(top_left_point, bottom_right_point)
    rect.outline_width = outline_width
    full_fill(rect, fill_colour, outline_colour)
    rect.draw(window)
    
def draw_circ(window:Window,
              center:Point,
              radius:int,
              fill_colour:str,
              outline_colour:str="",
              *,
              outline_width:int=1):
    """
    Draws circle with parsed parameters onto given window.
    
    Parameters
    -----
    window : Window
        Window to draw rectangle into
    center : Point
        Point of center of circle
    radius : Point
        Radius of circle to draw
    fill_colour : str
        Colour to fill inside rectangle
    outline_colour : str, optional
        Colour to make the outline of rectangle (if left blank, rectangle will have no outline)
    outline_width : int, optional
        Determines width of shape's outline (default value of 0.5)

    Returns
    -----
    None
    
    See Also
    -----
    full_fill()
    """
    circ = Circle(center, radius)
    circ.outline_width = outline_width
    full_fill(circ, fill_colour, outline_colour)
    circ.draw(window)