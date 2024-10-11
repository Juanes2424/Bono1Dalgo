import matplotlib.pyplot as plt
import timeit
import random


def prim(grafo, n_nodes):
    visited = {}
    mst = []

    actual = 0

    while len(mst) != n_nodes - 1:
        visited[actual] = True
        peso_minimo = 10**8
        minimum_edge = None

        for src, weight in grafo[actual].items():
            if weight < peso_minimo and src not in visited:
                peso_minimo = weight
                minimum_edge = src

        if minimum_edge == None:
            break

        origen, to, weight = actual, minimum_edge, peso_minimo
        mst.append((origen, to, weight))
        del grafo[origen][to]

        actual = to


def plot_barchart(data):

    dataset_1 = data
    x1, y1 = zip(*dataset_1)

    plt.scatter(x1, y1, color="blue", label="Datos Experimentales")

    plt.xlabel("Nodes")
    plt.ylabel("Tiempo (seg)")
    plt.title("Tiempo de Ejecucion de Prim")
    plt.legend()

    plt.show()


def controller():
    data = []

    for nodes in range(100, 1100, 100):
        tiempo_total = 0

        for it in range(0, 10):
            grafo = {x: {} for x in range(nodes)}

            for src in range(nodes):
                edgeCount = 0

                while edgeCount != int(nodes / 10):
                    destino = random.randint(0, nodes - 1)

                    if destino not in grafo[src]:
                        peso = random.randint(1, 10)

                        grafo[src].update({destino: peso})
                        grafo[destino].update({src: peso})
                        edgeCount += 1

            elapsed_time = timeit.timeit(lambda: prim(grafo, nodes), number=1)
            tiempo_total += elapsed_time

        print(f"Nodes: {nodes}, Time: {tiempo_total:.6f} seconds")
        data.append((nodes, tiempo_total))

    plot_barchart(data)


controller()
