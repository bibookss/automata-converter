import unittest
from src.automaton.dfa import DFA
from src.automaton.nfa import NFA
from src.automaton.enfa import ENFA

class TestDFA(unittest.TestCase):
    def create_dfa(self):
        dfa = DFA()
        dfa.set_alphabet(['0', '1'])
        dfa.add_state('q0')
        dfa.add_state('q1')
        dfa.add_state('q2')
        dfa.add_state('q3')
        dfa.add_state('q4')
        dfa.add_state('q5')
        dfa.set_initial_state('q0')
        dfa.set_final_states(['q2', 'q5'])
        dfa.add_transition('0', 'q0', 'q1')
        dfa.add_transition('1', 'q0', 'q2')
        dfa.add_transition('1', 'q1', 'q3')
        dfa.add_transition('0', 'q1', 'q4')
        dfa.add_transition('0', 'q2', 'q4')
        dfa.add_transition('1', 'q2', 'q4')
        dfa.add_transition('0', 'q3', 'q5')
        dfa.add_transition('1', 'q3', 'q4')
        dfa.add_transition('0', 'q4', 'q4')
        dfa.add_transition('1', 'q4', 'q4')
        dfa.add_transition('0', 'q5', 'q4')
        dfa.add_transition('1', 'q5', 'q4')

        return dfa

    def test_dfa_0(self):
        dfa = self.create_dfa()
        self.assertTrue(dfa.traverse('010'))

    def test_dfa_1(self):
        dfa = self.create_dfa()
        self.assertFalse(dfa.traverse('101001011101'))

class TestNFA(unittest.TestCase):
    def create_nfa(self):
        nfa = NFA()
        nfa.set_alphabet(['0', '1'])
        nfa.add_state('q0')
        nfa.add_state('q1')
        nfa.add_state('q2')
        nfa.add_transition('0', 'q0', 'q0')
        nfa.add_transition('1', 'q0', 'q0')
        nfa.add_transition('1', 'q0', 'q1')
        nfa.add_transition('0', 'q1', 'q2')
        nfa.set_initial_state('q0')
        nfa.set_final_states(['q2'])

        return nfa
    
    def test_nfa_0(self):
        nfa = self.create_nfa()
        self.assertTrue(nfa.traverse('1010010111010'))

    def test_nfa_1(self):
        nfa = self.create_nfa()
        self.assertFalse(nfa.traverse('101001011101'))

class TestENFA(unittest.TestCase):
    def create_enfa_0(self):
        enfa = ENFA()
        enfa.set_alphabet(['0', '1'])
        enfa.add_state('q0')
        enfa.add_state('q1')
        enfa.add_state('q2')
        enfa.add_transition('e', 'q0', 'q1')
        enfa.add_transition('1', 'q0', 'q1')
        enfa.add_transition('0', 'q1', 'q1')
        enfa.add_transition('0', 'q1', 'q0')
        enfa.add_transition('e', 'q1', 'q2')
        enfa.set_final_states(['q2'])
        enfa.set_initial_state('q0')

        return enfa
    
    def test_enfa_0(self):
        enfa = self.create_enfa_0()
        self.assertTrue(enfa.traverse('10100101010'))

    def test_enfa_1(self):
        enfa = self.create_enfa_0()
        self.assertTrue(enfa.traverse('e'))

    def test_enfa_2(self):
        enfa = self.create_enfa_0()
        self.assertTrue(enfa.traverse('00'))

    def test_enfa_3(self):
        enfa = self.create_enfa_0()
        self.assertTrue(enfa.traverse('001'))

    def test_enfa_4(self):
        enfa = self.create_enfa_0()
        self.assertTrue(enfa.traverse('101'))

    def test_enfa_5(self):
        enfa = self.create_enfa_0()
        self.assertFalse(enfa.traverse('11'))

    def create_enfa_1(self):
        enfa = ENFA()
        enfa.set_alphabet(['a', 'b'])
        enfa.add_state('q0')
        enfa.add_state('q1')
        enfa.add_state('q2')
        enfa.add_transition('e', 'q0', 'q1')
        enfa.add_transition('a', 'q0', 'q2')
        enfa.add_transition('b', 'q1', 'q2')
        enfa.add_transition('a', 'q2', 'q1')
        enfa.set_initial_state('q0')
        enfa.set_final_states(['q2'])

        return enfa
    
    def test_enfa_6(self):
        enfa = self.create_enfa_1()
        self.assertTrue(enfa.traverse('a'))
        
    def test_enfa_7(self):
        enfa = self.create_enfa_1()
        self.assertTrue(enfa.traverse('b'))

    def test_enfa_8(self):
        enfa = self.create_enfa_1()
        self.assertTrue(enfa.traverse('aab'))

    def test_enfa_9(self):
        enfa = self.create_enfa_1()
        self.assertTrue(enfa.traverse('bab'))

    def test_enfa_10(self):
        enfa = self.create_enfa_1()
        self.assertTrue(enfa.traverse('aabab'))

    def test_enfa_11(self):
        enfa = self.create_enfa_1()
        self.assertFalse(enfa.traverse('aa'))

    def test_enfa_12(self):
        enfa = self.create_enfa_1()
        self.assertFalse(enfa.traverse('bb'))

    def test_enfa_13(self):
        enfa = self.create_enfa_1()
        self.assertFalse(enfa.traverse('ba'))

    def test_enfa_14(self):
        enfa = self.create_enfa_1()
        self.assertFalse(enfa.traverse('e'))

if __name__ == '__main__':
    unittest.main()