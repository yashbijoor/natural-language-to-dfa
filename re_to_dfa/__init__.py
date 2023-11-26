__all__=['re_to_dfa']

from .utils import infix_to_postfix,add_concat,supercharge,regex_toStr
from .syntaxtree import SyntaxTree
from .dfa import DfaBuilder
from .visualize_dfa import visualize


def re_to_dfa(charset, regex):
    rgx=infix_to_postfix(add_concat(supercharge(regex)))
    tree=SyntaxTree(rgx)
    dfa=DfaBuilder().from_syntax_tree(tree)
    base64_dfa = visualize(charset, dfa)
    return dfa, base64_dfa
