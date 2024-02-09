__all__=['explanations_lib']

from .createExp import createExp

def explanations_lib(char_dictionary):
    explanations = createExp(char_dictionary)
    return explanations