#!/usr/bin/python3
""" A function to calculate the amount of water stored"""
def rain(walls):
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            left_max = max(left_max, walls[left])
            water += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            water += right_max - walls[right]
            right -= 1

    return water
