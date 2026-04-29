const API_URL = process.env.NEXT_PUBLIC_API_URL!;

export type GridPoint = {
  alpha: number;
  strong_force: number;
  habitability: number;
};

export async function simulateUniverse(params: any) {
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

export async function getUniverseGrid(): Promise<GridPoint[]> {
  const res = await fetch(`${API_URL}/grid`);

  if (!res.ok) {
    throw new Error("Grid fetch failed");
  }

  return res.json();
}