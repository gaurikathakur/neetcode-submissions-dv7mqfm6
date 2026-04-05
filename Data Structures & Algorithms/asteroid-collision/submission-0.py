class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            while stack and asteroid <0<stack[-1]:
                if stack[-1]<abs(asteroid):
                    stack.pop()
                    continue 
                elif stack[-1]==abs(asteroid):
                    stack.pop()
                break
            else:

                stack.append(int(asteroid))
        return stack



        