class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        """

        car 1 --> car 2 --> car 3.....car n
        position = []---length n , position [i] --> position of ith car
        speed = [] -- length n , speed [i] --> speed of ith car

        given target = positoin[target] miles 

        a car cannot pass but can catch up and drive same speed

        if a car catches up to a car, the car is considered to be part of fleet

        return the number of different car fleets that will arrive at destination
        """
        cars = [[p,s] for p,s in zip(position,speed)]

        stack = []

        for p,s in sorted(cars)[::-1]: # accessing from end for stack
            time_taken = (target - p)/s
            if not stack or time_taken > stack[-1]:
                stack.append(time_taken)

        return len(stack)

        