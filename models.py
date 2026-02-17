from sheets import load_pilots, load_drones, load_missions

def get_pilots():
    return load_pilots()

def get_drones():
    return load_drones()

def get_missions():
    return load_missions()
