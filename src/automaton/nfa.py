from .automaton import Automaton

class NFA(Automaton):
    def get_next_states(self, input, state):
        if self.transitions.get(state) is None:
            return None

        states = []
        for transition in self.transitions[state]:
            if transition[0] == input:
                states.append(transition[1])
        
        return states
    
    def traverse(self, string):
        active_states = {self.initial_state}
        for input in string:
            print('Current states: ', active_states)
            print('Input: ', input)

            states = set()
            for state in active_states:
                next_state = self.get_next_states(input, state)
                if next_state is not None:
                    states.update(next_state)

            if states is None:
                print('No transition found for input: ', input)
            else:
                active_states = states
            
            print('Arrived at states: ', active_states)

        for state in active_states:
            if state in self.final_states:
                print('String accepted')
                return True
        
        print('String not accepted')
        return False