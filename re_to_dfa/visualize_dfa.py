from graphviz import Digraph
import base64

class DFA:
	def __init__(self, no_state, states, no_alphabet, alphabets, start, no_final, finals, no_transition, transitions):
		self.no_state = no_state
		self.states = states
		self.no_alphabet = no_alphabet
		self.alphabets = alphabets
		
		self.start = start
		self.no_final = no_final
		self.finals = finals
		self.no_transition = no_transition
		self.transitions = transitions
		self.graph = Digraph()

		# Dictionaries to get index of states or alphabets
		self.states_dict = dict()
		for i in range(self.no_state):
			self.states_dict[self.states[i]] = i
		self.alphabets_dict = dict()
		for i in range(self.no_alphabet):
			self.alphabets_dict[self.alphabets[i]] = i
			
		# transition table is of the form
		self.transition_table = dict()
		for i in range(self.no_state):
			for j in range(self.no_alphabet):
				self.transition_table[str(i)+str(j)] = []
		for i in range(self.no_transition):
			self.transition_table[str(self.states_dict[self.transitions[i][0]]) + str(self.alphabets_dict[ self.transitions[i][1]])].append(self.states_dict[self.transitions[i][2]])
			

def visualize(charset, dfa):
	list_of_transitions = []
	for transition in dfa.transition_table.items():
		transition_list = list(transition[1].items())
		for item in transition_list:
			temp_list = []
			temp_list.append(transition[0])
			temp_list.append(item[0])
			temp_list.append(item[1])
			list_of_transitions.append(temp_list)
	no_of_states = len(dfa.transition_table.keys())
	no_of_alphabets = len(charset)
	list_of_states = list(dfa.transition_table.keys())
	start_state = dfa.startstate
	no_of_final_states = len(dfa.finalstates)
	list_of_final_states = list(dfa.finalstates)
	no_of_transitions = len(list_of_transitions)
	updated_dfa = DFA( no_of_states, list_of_states, no_of_alphabets, charset, start_state, no_of_final_states, list_of_final_states, no_of_transitions, list_of_transitions )

    # Making an object of Digraph to visualize the DFA diagram
	updated_dfa.graph = Digraph()
	updated_dfa.graph.graph_attr['rankdir'] = 'LR'
    # Adding states/nodes in DFA diagram
	for x in updated_dfa.states:
		# If state is not a final state, then border shape is single circle
		# Else it is double circle
		if (x not in updated_dfa.finals):
			updated_dfa.graph.attr('node', shape='circle')
			updated_dfa.graph.node(x)
		else:
			updated_dfa.graph.attr('node', shape='doublecircle')
			updated_dfa.graph.node(x)

	# Adding start state arrow in the DFA diagram
	updated_dfa.graph.attr('node', shape='none')
	updated_dfa.graph.node('')
	updated_dfa.graph.edge('', updated_dfa.start)

	# Adding edges between states in the DFA from the transitions array
	for x in updated_dfa.transitions:
		updated_dfa.graph.edge(x[0], x[2], label=(x[1]))

	image_data = updated_dfa.graph.pipe(format='png')

	return base64.b64encode(image_data).decode('utf-8')