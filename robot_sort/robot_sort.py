class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        """
        UNDERSTAND the problem:
        A robot needs to sort the items in a given list. His abilities include to turn his light on or off, move left or right
        (depending on whether he CAN move left or right depending on his position) and can compare and swap items.
        His attributes include the list as a parameter, an item that is defaulted to None (he's not holding on initially),
        position of 0 that we can use as a starting position inside the list, and a light with a default value of "OFF".
        We are also given a "time" attribute which I think we can use to count the number of steps it takes to sort the list. 
        To be honest, I'm not too sure how the robot's light should work or what its function in the algorithm should be, 
        but perhaps we could use it to indicate when the robot is active in sorting the list (i.e. "ON" when the list still 
        has unsorted values, and "OFF" when the list is completely sorted). 

        Since our "swap_item" method looks like it can only work on 2 consecutive items, this is very similar to a BUBBLE-type
        sorting solution. Very inefficient and definitely not ideal, but we work within our constraints. 

        PLAN a solution:
        1. Turn the light on by using "set_light_on" method.
        2. Check if the position has any value. If not, then return None or 0.
        3. If there was a value for the first position, check if we can move right by using method "can_move_right". 
            a. If we cannot, then the list has only 1 item and is thereby already sorted.
               The robot can turn his light off and return the 1-item list. 
            b. If we can move right, then store the value of the first item in memory for later comparison.
        4. If we can, move right by using "move_right" method. Check the value of the second item on the list. Compare that 
           value with the value stored from the previous item by using method "compare_value".
            a. If the value of the second item is greater than the value of the first item, repeat step 3 and move on to the
               next position on the right. 
            b. If the value of the second item is less than the value of the first item, perform "swap_item".
        5. Repeat steps 3 & 4 until we hit the end of the list, or "can_move_right" is no longer true. 
        6. Move all the way left with "move_left" until "can_move_left" is no longer true, indicating that we've reached the
           the beginning of the list again.
        7. Repeat steps 3-6 until the list is entirely sorted and "swap_item" is not triggered. 
        8. Turn the light off. 
        """
        pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)