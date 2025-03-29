# coding: utf-8

import cv2
import numpy as np
import math
def calculate_time(line_hour, line_minute, center):
    line_hour_center = (
        (line_hour[0, 0] + line_hour[0, 2]) // 2,
        (line_hour[0, 1] + line_hour[0, 3]) // 2,
    )
    line_minute_center = (
        (line_minute[0, 0] + line_minute[0, 2]) // 2,
        (line_minute[0, 1] + line_minute[0, 3]) // 2,
    )

    line_hour_center_from_clock_center = (
        center[0] - line_hour_center[0],
        center[1] - line_hour_center[1],
    )
    line_minute_center_from_clock_center = (
        center[0] - line_minute_center[0],
        center[1] - line_minute_center[1],
    )

    line_hour_angle = math.degrees(
        math.atan2(
            line_hour_center_from_clock_center[1], line_hour_center_from_clock_center[0]
        )
    )
    line_hour_angle = (line_hour_angle - 90) % 360
    line_minute_angle = math.degrees(
        math.atan2(
            line_minute_center_from_clock_center[1],
            line_minute_center_from_clock_center[0],
        )
    )
    line_minute_angle = (line_minute_angle - 90) % 360

    hour = line_hour_angle / 30 % 12
    minute = line_minute_angle / 6 % 60
    minute = round(minute / 5) * 5
    if minute == 60:
        minute = 0
        if hour == 3:
            hour += 1
    return f"{round(hour):02d}:{minute:02d}"
