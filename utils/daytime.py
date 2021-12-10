def whichPartOfDay(hour: int) -> str:
    if hour >= 0 and hour <= 12:
        return "morning"

    elif hour > 12 and hour <= 16:
        return "afternoon"

    else:
        return "evening"