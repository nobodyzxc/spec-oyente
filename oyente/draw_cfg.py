import graphviz as gv
import functools

def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

def create_graph(n, e, filename):
    digraph = functools.partial(gv.Digraph, format='svg')
    g = add_edges(add_nodes(digraph(), n), e)
    g.render(filename=filename, cleanup=True)
    return g

def cfg_nodes(blocks, lgp, show_cond):
    color = lambda tag, cover: '#f4f141' if tag in lgp else ('' if cover else '#ffffff')
    return [(str(block.start), \
             { 'label' : \
                 'start: ' + str(block.start) + '\n' +
                 ('\n'.join(block.inst_gas) if block.inst_gas \
                         else '\n'.join(block.instructions)) +
                 '\nend : ' + str(block.end) + '\n' + \
                 ('gas : ' + str(block.gas) + '\n' if block.inst_gas else '') + \
                 ('acc_gas : ' + str(block.acc_gas) + '\n' if block.acc_gas else '') + \
                 ('constraints : ' + block.path_cond if block.path_cond and show_cond else ''), \
                'shape': 'box', \
                'style': 'filled', \
                'fillcolor': color(block.start, block.inst_gas),
             }) for block in blocks]

def cfg_edges(es, lgp):
    les = list(zip(lgp[:-1], lgp[1:]))
    es = [(b, e) for b in es for e in es[b]]
    return [((str(b), str(e)),
            {'label' : '',
             'color': 'red' if (b, e) in les else 'blue'
            }) for (b, e) in es]
