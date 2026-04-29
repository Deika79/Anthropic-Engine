export type UniverseParameters = {
  alpha: number;
  strong_force: number;
  electron_mass: number;
  cosmological_constant: number;
};

export type SimulationResult = {
  star_stability: boolean;
  heavy_elements: boolean;
  chemistry_score: number;
  habitability_score: number;
  explanation: string;
};

export type GridPoint = {
  alpha: number;
  strong_force: number;
  habitability: number;
};

const API_URL = "http://127.0.0.1:8001";

// 🔬 Single simulation
export async function simulateUniverse(
  params: UniverseParameters
): Promise<SimulationResult> {
  const res = await fetch(`${API_URL}/simulate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(params),
  });

  if (!res.ok) {
    throw new Error("Simulation failed");
  }

  return res.json();
}

// 🌌 Grid simulation
export async function getUniverseGrid(): Promise<GridPoint[]> {
  const res = await fetch(`${API_URL}/grid`);

  if (!res.ok) {
    throw new Error("Grid fetch failed");
  }

  return res.json();
}