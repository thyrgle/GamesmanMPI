import src.utils

X = src.utils.game_module.X
O = src.utils.game_module.O
BLANK = src.utils.game_module.BLANK

def tie_in_one():
    return  X + X + O + \
            O + O + X + \
            X + O + BLANK

def win_in_one():
	return X + X + BLANK + \
           O + O + X + \
           X + O + O
