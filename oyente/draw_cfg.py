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

def create_graph(n, e):
    # print('[INFO] Constructing visualizing graph')
    digraph = functools.partial(gv.Digraph, format='svg')
    g = add_edges(add_nodes(digraph(), n), e)
    #filename = 'img/{}/g{}'.format(row_id, row_id)
    g.render(filename='cfg')
    # print('[COMPLETE - CFG construction]')

    return g

def cfg_nodes(blocks):
    return [(str(block.start), \
             { 'label' : \
                 'start: ' + str(block.start) + '\n' + \
                 '\n'.join(block.instructions) +
                 '\nend : ' + str(block.end) , \
                'shape': 'box' \
             }) for block in blocks]

def cfg_edges(es, lgp):
    les = list(zip(lgp[:-1], lgp[1:]))
    es = [(b, e) for b in es for e in es[b]]
    print(lgp)
    print(es)
    #for t in es:
    #    print(t, ' : ', t in les, '>>', les)
    return [((str(b), str(e)),
            {'label' : '',
             'color': 'red' if (b, e) in les else 'blue'
            }) for (b, e) in es]
    #edges = []
    #for k in es:
    #    for nxt in es[k]:
    #        edges.append(
    #                ((str(k), str(nxt)),
    #                    {'label' : '',
    #                        'color': 'blue'}))
    #return edges
