import matplotlib.pyplot as plt
import timeit
import random
import heapq


def dijkstra(grafo):
    rutas = {}
    costos = {}
    visitados = {}

    pq = [(0, 0)]
    costos[0] = 0
    rutas[0] = None

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node in visitados:
            continue

        visitados[current_node] = True

        for neighbor, weight in grafo[current_node].items():
            new_cost = current_cost + weight

            if neighbor not in costos or new_cost < costos[neighbor]:

                costos[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
                rutas[neighbor] = current_node

    return rutas


def plot_barchart(data):

    dataset_1 = data
    x1, y1 = zip(*dataset_1)

    plt.scatter(x1, y1, color="blue", label="Datos Experimentales")

    plt.xlabel("Nodes + Edges")
    plt.ylabel("Tiempo (seg)")
    plt.title("Tiempo de Ejecucion de Dijkstra")
    plt.legend()

    plt.show()


def controller():
    data = []
    UT = 0
    for nodes in range(100000, 1100000, 100000):
        tiempo_total = 0

        for it in range(0, 10):
            grafo = {x: {} for x in range(nodes)}
            edges = nodes

            edgeCount = 0

            while edgeCount != edges:
                src = random.randint(0, nodes - 1)
                destino = random.randint(0, nodes - 1)

                if destino not in grafo[src]:
                    grafo[src].update({destino: 1})
                    edgeCount += 1

            elapsed_time = timeit.timeit(lambda: dijkstra(grafo), number=1)
            tiempo_total += elapsed_time

        if nodes == 100000:
            UT = tiempo_total

        print(f"Nodes: {nodes}, Time: {tiempo_total:.6f} seconds")
        data.append((nodes * 2, tiempo_total))

    plot_barchart(data)


controller()
