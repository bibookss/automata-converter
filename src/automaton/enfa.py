from automaton.automaton import Automaton

class ENFA(Automaton):
    def get_next_states(self, input, state):
        if self.transitions.get(state) is None:
            return None

        states = []
        for transition in self.transitions[state]:
            if transition[0] == input:
                states.append(transition[1])
        
        return states
    
    def traverse(self, string):
        active_states = [self.initial_state]
        for input in string:
            print('Current states: ', active_states)
            print('Input: ', input)

            states = []
            for state in active_states:
                next_state = self.get_next_states(input, state)
                if next_state is not None:
                    states.extend(next_state)

            if states is None:
                print('No transition found for input: ', input)
            else:
                active_states = states
            
            print('Arrived at states: ', active_states)

        for state in active_states:
            is_final_state = self.is_final_state(state)
            if is_final_state:
                print('String accepted')
                return
        
        print('String not accepted')