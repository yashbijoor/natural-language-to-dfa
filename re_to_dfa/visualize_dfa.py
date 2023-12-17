from graphviz import Digraph
import base64


def visualize(dfa):
	list_of_transitions = []
	list_of_images = []
	total_states = list(dfa.transition_table.keys())
	count = 2

	# Making an object to visualize the DFA diagram
	graph = Digraph()
	graph.graph_attr['rankdir'] = 'LR'
	
	# Add start state node in the DFA diagram
	graph.attr('node', shape='circle')
	graph.node('s0')

	# Adding start state arrow in the DFA diagram
	graph.attr('node', shape='none')
	graph.node('')
	graph.edge('', 's0')

	image_data = graph.pipe(format='png')
	list_of_images.append("data:image/png;base64," + base64.b64encode(image_data).decode('utf-8'))

	for transition in dfa.transition_table.items():
		transition_list = list(transition[1].items())
		for item in transition_list:
			temp_list = []
			temp_list.append(transition[0])
			temp_list.append(item[0])
			temp_list.append(item[1])
			list_of_transitions.append(temp_list)
		list_of_states = total_states[:count]
		start_state = dfa.startstate

		if len(list_of_states) == len(dfa.transition_table.keys()):
			list_of_final_states = list(dfa.finalstates)
		else:
			list_of_final_states = []
		
		# Making an object to visualize the DFA diagram
		graph = Digraph()
		graph.graph_attr['rankdir'] = 'LR'

		# Adding states/nodes in DFA diagram
		for x in list_of_states:
			# If state is not a final state, then border shape is single circle
			# Else it is double circle
			if (x not in list_of_final_states):
				graph.attr('node', shape='circle')
				graph.node(x)
			else:
				graph.attr('node', shape='doublecircle')
				graph.node(x)

		# Adding start state arrow in the DFA diagram
		graph.attr('node', shape='none')
		graph.node('')
		graph.edge('', start_state)

		# Adding edges between states in the DFA from the transitions array
		for x in list_of_transitions:
			graph.edge(x[0], x[2], label=(x[1]))

		image_data = graph.pipe(format='png')
		list_of_images.append("data:image/png;base64," + base64.b64encode(image_data).decode('utf-8'))
		count += 1

	return list_of_images