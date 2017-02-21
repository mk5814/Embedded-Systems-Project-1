def pointing(direction):
    if direction >= 22.5 and direction < 67.5:
        return 'north east'
    elif direction >= 67.5 and direction < 112.5:
        return 'east'
    elif direction >= 112.5 and direction < 157.5:
        return 'south east'
    elif direction >= 157.5 and direction < 202.5:
        return 'south'
    elif direction >= 202.5 and direction < 247.5:
        return 'south west'
    elif direction >= 247.5 and direction < 292.5:
        return 'west'
    elif direction >= 292.5 and direction < 337.5:
        return 'north west'
    else:
        return 'north'
