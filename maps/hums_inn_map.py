from settings import *
from gamestates.states import *

walls     = [[w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,w,w,w,w,w,w,w,w,w,w,w,w,w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,w],
			 [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,d,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w]]

doors = [HUMS_STATE]
entrances = [[10, 5]]
npcs = {"Innkeeper": {"x": 7, "y": 6, "direction": SOUTH, "hail_range": 2}}