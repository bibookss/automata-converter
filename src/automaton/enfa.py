from automaton.nfa import NFA

class ENFA(NFA):
    def __init__(self):
        super().__init__()
        self.alphabet.add('e')

    def set_alphabet(self, alphabet):
        self.alphabet.update(alphabet)

    def get_next_states(self, input, state):
        if self.transitions.get(state) is None:
            return None

        states = []
        for transition in self.transitions[state]:
            if transition[0] == input:
                states.append(transition[1])
        
        if len(states) == 0:
            return None

        return states
    
    def traverse(self, string):
        length = len(string)
        active_states = {self.initial_state}
        
        for input in string:
            # Get epsilon states from current active states and add them to active states
            _active_states = list(active_states)
            for state in _active_states:
                _epsilon_states = self.get_next_states('e', state)
                if _epsilon_states is not None:
                    _active_states.extend(_epsilon_states)

            active_states = set(_active_states)
            print('Current states: ', active_states)

            # For each active state, get next states for input and add them to active states
            states = set()
            _active_states = list(active_states)
            for state in _active_states:
                next_states = self.get_next_states(input, state)
                epsilon_states = self.get_next_states('e', state)
                if next_states is not None:
                    states.update(next_states)

                    length -= 1
                    print('From state: ', state)
                    print('Consumed input: ', input)
                    print('Next states: ', next_states)

                    # Remove from state 
                    if state in states:
                        states.remove(state)

                if epsilon_states is not None:
                    states.update(epsilon_states)
        
            active_states = states

        print('Final active states: ', active_states)
        print('Remaining length: ', length)
        for state in active_states:
            if state in self.final_states and not length > 0:
                print('String accepted')
                return
            
        print('String not accepted')