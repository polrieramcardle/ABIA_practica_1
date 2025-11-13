import math
import random
from dataclasses import dataclass
from typing import List, Tuple, Dict

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # per al 3D bar


# --------------------------------------------------------------------
# 1. Definició del TSP aleatori
# --------------------------------------------------------------------

@dataclass
class TSPInstance:
    coords: np.ndarray        # shape: (n, 2)
    dist: np.ndarray          # shape: (n, n)

def generate_random_tsp(n_cities: int, seed: int = 1234) -> TSPInstance:
    rnd = random.Random(seed)
    coords = np.array([[rnd.random(), rnd.random()] for _ in range(n_cities)])
    n = n_cities
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist[i, j] = math.dist(coords[i], coords[j])
    return TSPInstance(coords=coords, dist=dist)


def route_cost(route: List[int], inst: TSPInstance) -> float:
    """Cost total de la ruta (cicle tancat)."""
    d = inst.dist
    c = 0.0
    n = len(route)
    for i in range(n - 1):
        c += d[route[i], route[i + 1]]
    c += d[route[-1], route[0]]
    return c


def random_route(n: int, rnd: random.Random) -> List[int]:
    r = list(range(n))
    rnd.shuffle(r)
    return r


def neighbor_swap(route: List[int], rnd: random.Random) -> List[int]:
    """Veí simple: intercanvi de dues ciutats."""
    n = len(route)
    i, j = rnd.sample(range(n), 2)
    new = route.copy()
    new[i], new[j] = new[j], new[i]
    return new


# --------------------------------------------------------------------
# 2. Hill Climbing i Simulated Annealing
# --------------------------------------------------------------------

def hill_climbing(
    inst: TSPInstance,
    initial_route: List[int],
    max_iter: int,
    rnd: random.Random
) -> Tuple[List[int], float, List[float]]:
    current = initial_route
    current_cost = route_cost(current, inst)
    costs = [current_cost]

    for _ in range(max_iter):
        candidate = neighbor_swap(current, rnd)
        cand_cost = route_cost(candidate, inst)
        if cand_cost < current_cost:
            current, current_cost = candidate, cand_cost
        costs.append(current_cost)

    return current, current_cost, costs


def simulated_annealing(
    inst: TSPInstance,
    initial_route: List[int],
    max_iter: int,
    k: float,
    lam: float,
    rnd: random.Random
) -> Tuple[List[int], float, List[float]]:
    """
    SA amb schedule exponencial: T(t) = k * exp(-lam * t)
    """
    current = initial_route
    current_cost = route_cost(current, inst)
    best = current
    best_cost = current_cost
    costs = [current_cost]

    for t in range(1, max_iter + 1):
        T = k * math.exp(-lam * t)
        if T <= 1e-12:
            T = 1e-12  # evitar underflow

        candidate = neighbor_swap(current, rnd)
        cand_cost = route_cost(candidate, inst)
        delta = cand_cost - current_cost

        if delta < 0 or rnd.random() < math.exp(-delta / T):
            current, current_cost = candidate, cand_cost

        if current_cost < best_cost:
            best, best_cost = current, current_cost

        costs.append(current_cost)

    return best, best_cost, costs


# --------------------------------------------------------------------
# 3. Experiments: HC vs SA, variar k, variar λ, grid k×λ
# --------------------------------------------------------------------

def experiment_hc_vs_sa():
    """
    Reprodueix una gràfica tipus Figura 6.7:
    evolució del cost per HC i SA sobre la mateixa instància i
    la mateixa ruta inicial.
    """
    n_cities = 351
    seed = 1234
    inst = generate_random_tsp(n_cities, seed)
    rnd = random.Random(seed)

    init_route = random_route(n_cities, rnd)

    # Paràmetres de l'exemple: It=1000, k=5, λ=0.01
    max_iter = 1000
    k = 5.0
    lam = 0.01

    _, cost_hc, costs_hc = hill_climbing(inst, init_route, max_iter, rnd)
    rnd2 = random.Random(seed)  # per fer SA des de la mateixa ruta
    _, cost_sa, costs_sa = simulated_annealing(inst, init_route, max_iter, k, lam, rnd2)

    plt.figure(figsize=(7, 5))
    plt.plot(costs_hc, label="HC", color="tab:blue")
    plt.plot(costs_sa, label="SA", color="tab:red")
    plt.xlabel("Passos")
    plt.ylabel("Cost")
    plt.title("Evolució del cost: HC vs SA")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def experiment_vary_k():
    """
    Equivalent a figura 6.9: evolució del cost per diferents k
    (mateix λ i mateix nombre d'iteracions).
    """
    n_cities = 351
    seed = 1234
    inst = generate_random_tsp(n_cities, seed)

    ks = [1, 5, 25, 125]
    lam = 0.1
    max_iter = 10000

    plt.figure(figsize=(7, 8))

    for idx, k in enumerate(ks, start=1):
        rnd = random.Random(seed)
        init_route = random_route(n_cities, rnd)
        _, _, costs_sa = simulated_annealing(inst, init_route, max_iter, k, lam, rnd)

        plt.subplot(len(ks), 1, idx)
        plt.plot(costs_sa, color="tab:red")
        plt.xlabel("Passos")
        plt.ylabel("Cost")
        plt.title(f"Evolució del cost (SA) – It={max_iter}, k={k}, λ={lam}")
        plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()


def experiment_vary_lambda():
    """
    Equivalent a figura 6.10: evolució del cost per diferents λ,
    mantenint k fix.
    """
    n_cities = 351
    seed = 1234
    inst = generate_random_tsp(n_cities, seed)

    k = 5.0
    lams = [0.001, 1e-4, 1e-5]
    max_iter = 300000

    plt.figure(figsize=(7, 8))

    for idx, lam in enumerate(lams, start=1):
        rnd = random.Random(seed)
        init_route = random_route(n_cities, rnd)
        _, _, costs_sa = simulated_annealing(inst, init_route, max_iter, k, lam, rnd)

        plt.subplot(len(lams), 1, idx)
        plt.plot(costs_sa, color="tab:red")
        plt.xlabel("Passos")
        plt.ylabel("Cost")
        plt.title(f"Evolució del cost (SA) – It={max_iter}, k={k}, λ={lam}")
        plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()


def experiment_prob_acceptance():
    """
    Versió simple de la figura 6.6: probabilitat d'acceptar un moviment
    amb increment de cost ΔE=1, per diferents λ, al llarg de les iteracions.
    """
    max_iter = 10000
    k = 10.0
    lams = [0.0005, 0.001, 0.01, 0.1]

    iters = np.arange(max_iter)
    plt.figure(figsize=(7, 5))
    for lam in lams:
        T = k * np.exp(-lam * iters)
        prob = np.exp(-1.0 / T)  # ΔE=1
        plt.plot(iters, prob, label=f"exp(-1/(10*exp(-{lam}*x)))")

    plt.xlabel("Iteració")
    plt.ylabel("Probabilitat")
    plt.title("Variació del comportament variant λ")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def experiment_grid_k_lambda():
    """
    Equivalent conceptual a figura 6.11: per a cada combinació de k i λ
    executa diverses rèpliques i mostra el cost mitjà final en un 3D bar
    o bé un heatmap.
    """
    n_cities = 351
    seed_base = 1234
    inst = generate_random_tsp(n_cities, seed_base)

    ks = [1, 5, 25, 125]
    lams = [1.0, 0.01, 0.0001]
    max_iter = 100000
    repeats = 5

    mean_costs = np.zeros((len(ks), len(lams)))

    for i, k in enumerate(ks):
        for j, lam in enumerate(lams):
            costs = []
            for r in range(repeats):
                rnd = random.Random(seed_base + r)
                init_route = random_route(n_cities, rnd)
                _, best_cost, _ = simulated_annealing(
                    inst, init_route, max_iter, k, lam, rnd
                )
                costs.append(best_cost)
            mean_costs[i, j] = np.mean(costs)
            print(f"k={k:<4} λ={lam:<8} -> cost mitjà {mean_costs[i, j]:.2f}")

    # 3D bar plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    xpos, ypos = np.meshgrid(np.arange(len(ks)), np.arange(len(lams)), indexing="ij")
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)

    dx = dy = 0.4 * np.ones_like(xpos)
    dz = mean_costs.flatten()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)
    ax.set_xticks(np.arange(len(ks)) + 0.2)
    ax.set_xticklabels(ks)
    ax.set_yticks(np.arange(len(lams)) + 0.2)
    ax.set_yticklabels(lams)
    ax.set_xlabel("k")
    ax.set_ylabel("λ")
    ax.set_zlabel("Cost mitjà")
    ax.set_title("Variació del cost per SA per diversos valors de k i λ")
    plt.tight_layout()
    plt.show()

    # Alternativament, heatmap:
    plt.figure(figsize=(6, 4))
    plt.imshow(mean_costs, cmap="viridis", origin="lower")
    plt.colorbar(label="Cost mitjà")
    plt.xticks(range(len(lams)), lams)
    plt.yticks(range(len(ks)), ks)
    plt.xlabel("λ")
    plt.ylabel("k")
    plt.title("Heatmap del cost mitjà (SA)")
    plt.tight_layout()
    plt.show()


# --------------------------------------------------------------------
# 4. Exemple d’ús
# --------------------------------------------------------------------

if __name__ == "__main__":
    # Tria quins experiments vols llançar:
    experiment_hc_vs_sa()
    experiment_vary_k()
    experiment_vary_lambda()
    experiment_prob_acceptance()
    experiment_grid_k_lambda()
