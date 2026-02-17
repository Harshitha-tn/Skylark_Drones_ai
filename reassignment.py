from assignment import match_pilots

def urgent_reassign(mission):
    alternatives = match_pilots(mission)

    if alternatives.empty:
        return None

    return alternatives.iloc[0]