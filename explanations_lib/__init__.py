__all__=['explanations_lib']

from .createExp import createExp

def explanations_lib(char_dictionary, charset):
    explanations = createExp(char_dictionary, charset) #Calls createExp funtion where the explanation logic lies
    return explanations