from aima3.search import simulated_annealing
try:
    from aima3.search import exp_schedule
except Exception:
    exp_schedule = None

from implementacio.camions_problema import CamionsProblema
from implementacio.camions_parametres import ProblemParameters
from implementacio.camions_estat import generate_initial_state
from implementacio.abia_Gasolina import Gasolineres, CentresDistribucio
import time
import json
from statistics import mean
import multiprocessing as mp
import os
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------
# Configuració del problema
# ----------------------------------------
NUM_GASOLINERES = 100
NUM_CENTRES = 10
SEED_BASE = 1234

params_template = {
    "km": 640,
    "n_viatges": 5,
    "valor": 1000,
    "cost_km": 2,
}

# ----------------------------------------
# Espai de paràmetres per simulated annealing
# ----------------------------------------
limits = [200, 500, 1000]
ks = [1, 10, 20, 50]
lams = [0.001, 0.003, 0.005, 0.01]
REPEATS = 10

OUTFILE = "sa_param_search_results.json"
TEMP_OUT = OUTFILE + ".partial.json"

# ----------------------------------------
# Funció auxiliar: una sola execució
# ----------------------------------------
def run_single(cfg):
    limit, k, lam, rep = cfg
    seed = SEED_BASE + rep
    gasolineres = Gasolineres(num_gasolineres=NUM_GASOLINERES, seed=seed)
    centres = CentresDistribucio(num_centres=NUM_CENTRES, multiplicitat=1, seed=seed)
    params = ProblemParameters(
        km=params_template["km"],
        n_viatges=params_template["n_viatges"],
        valor=params_template["valor"],
        cost_km=params_template["cost_km"],
        gasolineres=gasolineres,
        centres=centres
    )

    initial_state = generate_initial_state(params)
    problema = CamionsProblema(initial_state)

    try:
        problema.operadors = ["swapCentres", "mourePeticio", "intercanviaPeticio"]
    except Exception:
        try:
            problema.set_operadors(["swapCentres", "mourePeticio", "intercanviaPeticio"])
        except Exception:
            pass

    schedule = None
    if exp_schedule is not None:
        try:
            schedule = exp_schedule(k=k, lam=lam, limit=limit)
        except Exception:
            schedule = None

    start = time.perf_counter()
    try:
        if schedule is not None:
            sol = simulated_annealing(problema, schedule=schedule)
        else:
            sol = simulated_annealing(problema, limit=limit)
    except TypeError:
        sol = simulated_annealing(problema)
    end = time.perf_counter()
    dur_ms = (end - start) * 1000

    if sol is None:
        return {"limit": limit, "k": k, "lam": lam, "rep": rep,
                "mean_benefici": float("-inf"), "time_ms": dur_ms}

    try:
        ingressos = sol.calcular_ingressos_servits()
    except Exception:
        ingressos = 0.0
    try:
        cost_km = sol.calcular_cost_km()
    except Exception:
        cost_km = 0.0
    try:
        penalitzacio = sol.calcular_penalitzacio_pendents()
    except Exception:
        penalitzacio = 0.0

    benefici = ingressos - cost_km - penalitzacio
    return {"limit": limit, "k": k, "lam": lam, "rep": rep,
            "mean_benefici": benefici, "time_ms": dur_ms}


# ----------------------------------------
# Nova funció: gràfics de resultats (heatmap)
# ----------------------------------------
def plot_heatmaps(final_results):
    """Genera heatmaps de benefici mitjà per cada valor de limit."""
    limits = sorted(set(f["limit"] for f in final_results))
    ks = sorted(set(f["k"] for f in final_results))
    lams = sorted(set(f["lam"] for f in final_results))

    for limit in limits:
        matrix = np.full((len(ks), len(lams)), np.nan)
        for i, k in enumerate(ks):
            for j, lam in enumerate(lams):
                match = next((f for f in final_results if f["limit"] == limit and f["k"] == k and f["lam"] == lam), None)
                if match:
                    matrix[i, j] = match["mean_benefici"]

        # Normalitzar per destacar diferències relatives
        if np.nanmax(matrix) > np.nanmin(matrix):
            norm_matrix = (matrix - np.nanmin(matrix)) / (np.nanmax(matrix) - np.nanmin(matrix))
        else:
            norm_matrix = matrix

        fig, ax = plt.subplots(figsize=(7, 5))
        im = ax.imshow(norm_matrix, cmap="viridis", origin="lower", aspect="auto")
        ax.set_xticks(range(len(lams)))
        ax.set_yticks(range(len(ks)))
        ax.set_xticklabels(lams)
        ax.set_yticklabels(ks)
        ax.set_xlabel("λ (taxa de refredament)")
        ax.set_ylabel("k (escala temperatura inicial)")
        ax.set_title(f"Benefici relatiu (limit = {limit})")

        # Mostra els valors reals sobre el gràfic
        for i in range(len(ks)):
            for j in range(len(lams)):
                val = matrix[i, j]
                if not np.isnan(val):
                    ax.text(j, i, f"{val:.1f}", ha="center", va="center", color="black", fontsize=8)

        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label("Benefici relatiu (normalitzat)")
        plt.tight_layout()
        plt.savefig(f"heatmap_limit_{limit}.png", dpi=300)
        plt.show()


# ----------------------------------------
# Funció principal
# ----------------------------------------
def main():
    configs = []
    for limit in limits:
        for k in ks:
            for lam in lams:
                for rep in range(REPEATS):
                    configs.append((limit, k, lam, rep))

    manager = mp.Manager()
    results = []
    cpu_count = max(1, os.cpu_count() - 1)
    print(f"Executant {len(configs)} runs en paral·lel amb {cpu_count} processos...")

    with mp.Pool(processes=cpu_count) as pool:
        for i, res in enumerate(pool.imap_unordered(run_single, configs), 1):
            results.append(res)
            with open(TEMP_OUT, "w") as f:
                json.dump(results, f, indent=2)
            print(f"[{i}/{len(configs)}] limit={res['limit']} k={res['k']} lam={res['lam']} rep={res['rep']} -> ben={res['mean_benefici']:.2f} time={res['time_ms']:.0f}ms")

    summary = {}
    for r in results:
        key = (r["limit"], r["k"], r["lam"])
        summary.setdefault(key, []).append(r["mean_benefici"])
    final = []
    for (limit, k, lam), vals in summary.items():
        valid = [v for v in vals if v != float("-inf")]
        mean_ben = mean(valid) if valid else float("-inf")
        final.append({"limit": limit, "k": k, "lam": lam, "mean_benefici": mean_ben, "raw": vals})

    valid_final = [f for f in final if f["mean_benefici"] != float("-inf")]
    best = max(valid_final, key=lambda x: x["mean_benefici"]) if valid_final else None

    out = {"results": final, "best": best}
    with open(OUTFILE, "w") as f:
        json.dump(out, f, indent=2)
    try:
        os.remove(TEMP_OUT)
    except Exception:
        pass

    print("Cerca completada. Millor configuració:", best)

    # 🔥 Nou: genera els gràfics
    plot_heatmaps(final)


if __name__ == "__main__":
    main()
