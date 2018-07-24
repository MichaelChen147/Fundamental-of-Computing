Before:

def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    position[0] = (position[0] + vector[0]) % SCREEN_SIZE[0]
    position[1] = (position[1] + vector[1]) % SCREEN_SIZE[1]
    
After:

NUM_DIMENSIONS = 2
def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    for d in range(NUM_DIMENSIONS):
        position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]
        
################################################################

def move_dimension(dimension, position, vector):
    """Moves the position component by the given vector component in 1D toroidal space."""
    position[dimension] = (position[dimension] + vector[dimension]) % SCREEN_SIZE[dimension]

def move(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    move_dimension(0, position, vector)
    move_dimension(1, position, vector)
