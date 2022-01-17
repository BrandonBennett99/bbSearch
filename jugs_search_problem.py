

class JugsSearchProblem( SearchProblem ):
    
    def __init__( self ):
        self.initial_state = {"small":(3,0),
                              "medium":(5,0),
                              "large":  (8,8) }
        self.goal_quantity = 4
        print( "Creating SearchProblem object" )
        print( "Setting initial state to:", self.initial_state )
        print( "Want to measure quantity:", self.goal_quantity )
        
        self.jugs = self.initial_state.keys()

    def info(self):
        print( "Measuring Jugs problem: \n" )
            

    def possible_actions(self, state):
        actions = []
        for j1 in self.jugs:
            for j2 in self.jugs:
                if ( j1!=j2  #different jugs
                     and state[j1][1] > 0  # j1 not empty
                     and state[j2][0]>state[j2][1] # j2 not full
                   ): actions.append((j1,j2))
        return actions
                    
    def successor(self, state, action):
        new_state = { k:state[k] for k in state }
        j1, j2 = action[0], action[1]
        vol_in_j1 = state[j1][1]
        vol_in_j2 = state[j2][1]
        space_in_j2 = state[j2][0] - state[j2][1]
        if vol_in_j1 <= space_in_j2:
            new_j1 = 0
            new_j2 = vol_in_j1 + vol_in_j2
        else:
            new_j1 = vol_in_j1 - space_in_j2
            new_j2 = state[j2][0]
        new_state[j1] = (state[j1][0], new_j1)
        new_state[j2] = (state[j2][0], new_j2)
        return new_state

    def goal_test(self, state):
        #print(state)
        quantities = [ state[k][1] for k in state]
        return  self.goal_quantity in quantities

    def display_action( self, action ):
        j1, j2 = action
        print(f"Pour from {j1} to {j2}:")


    def display_state( self, state ):
        jug_quantities = [ f"{k}: {state[k][1]}({state[k][0]})" for k in state]
        print( ", ".join(jug_quantities))

        
