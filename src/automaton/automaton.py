class Automaton:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initial_state = None
        self.final_states = []
        self.transitions = {}

    def add_state(self, state):
        self.states.append(state)

    def add_transition(self, input, from_state, to_state):
        if self.transitions.get(from_state) is None:
            self.transitions[from_state] = []
        
        self.transitions[from_state].append((input, to_state))

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def set_initial_state(self, state):
        self.initial_state = state

    def set_final_states(self, states):
        self.final_states = states

    def get_next_state(self, input, state):
        for transition in self.transitions[state]:
            if transition[0] == input:
                return transition[1]
       
        return None
    
    def is_final_state(self, state):
        return state in self.final_states
    
    def traverse(self, string):
        state = self.initial_state
        for input in string:
            print('Current state: ', state)
            print('Input: ', input)
            state = self.get_next_state(input, state)
            if state is None:
                print('No transition found for input: ', input)
                break
            
            print('Arrived at state: ', state)
        
        print('Final state: ', state)

        is_final_state = self.is_final_state(state)
        if is_final_state:
            print('String accepted')
        else:
            print('String not accepted')