"""
1344. Angle Between Hands of a Clock
Medium

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

Example 1:

Input: hour = 12, minutes = 30
Output: 165
Example 2:

Input: hour = 3, minutes = 30
Output: 75
Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
"""
#85%
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_deg = hour*(360/12)+(minutes/60)*(360/12)
        minute_deg = minutes*360/60
        return min(abs(hour_deg-minute_deg),360-abs(hour_deg-minute_deg))

"""
Some precalculation and instead of min just checks if its greater than 180 degrees
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # Degree covered by hour hand (hour area + minutes area)
        h = (hour%12 * 30) + (minutes/60 * 30)
        
        # Degree covered by minute hand (Each minute = 6 degree)
        m = minutes * 6
        
        # Absolute angle between them
        angle = abs(m - h)
        
        # If the angle is obtuse (>180), convert it to acute (0<=x<=180)
        if angle > 180:
            angle = 360.0 - angle
        
        return (angle)
"""