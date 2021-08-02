

def diff(angle1, angle2):
    return min(
        (angle1 - angle2) % 360,
        (angle2 - angle1) % 360,
    )


print(diff(-30, 45))
print(diff(0, 180))
print(diff(0, 190))
print(diff(120, 280))
