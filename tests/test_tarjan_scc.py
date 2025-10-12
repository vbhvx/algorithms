from algorithms.graphs.tarjan_scc import tarjan_scc
def test_scc(): adj = {0: [1], 1: [2], 2: [0], 3: [1]}; assert len(tarjan_scc(4, adj)) == 2
