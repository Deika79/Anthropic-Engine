"use client";

import { useEffect, useState } from "react";
import {
  simulateUniverse,
  getUniverseGrid,
  UniverseParameters,
  SimulationResult,
  GridPoint,
} from "@/lib/api";

import UniverseMap from "@/components/UniverseMap";

export default function Home() {
  const [params, setParams] = useState<UniverseParameters>({
    alpha: 1,
    strong_force: 1,
    electron_mass: 1,
    cosmological_constant: 1,
  });

  const [result, setResult] = useState<SimulationResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [gridData, setGridData] = useState<GridPoint[]>([]);

  const [debouncedParams, setDebouncedParams] = useState(params);

  // ⏱ debounce
  useEffect(() => {
    const timeout = setTimeout(() => {
      setDebouncedParams(params);
    }, 300);

    return () => clearTimeout(timeout);
  }, [params]);

  // 🔬 simulación
  useEffect(() => {
    const runSimulation = async () => {
      setLoading(true);

      try {
        const res = await simulateUniverse(debouncedParams);
        setResult(res);
      } catch (err) {
        console.error(err);
      }

      setLoading(false);
    };

    runSimulation();
  }, [debouncedParams]);

  // 🌌 grid
  useEffect(() => {
    const loadGrid = async () => {
      try {
        const data = await getUniverseGrid();
        setGridData(data);
      } catch (err) {
        console.error(err);
      }
    };

    loadGrid();
  }, []);

  const handleChange = (key: keyof UniverseParameters, value: number) => {
    setParams((prev) => ({
      ...prev,
      [key]: value,
    }));
  };

  return (
    <main className="min-h-screen bg-black text-white p-10">
      <h1 className="text-3xl font-bold mb-6">
        Anthropic Engine
      </h1>

      {/* CONTROLES */}
      <div className="space-y-6 max-w-xl">

        <div>
          <label>Alpha: {params.alpha.toFixed(2)}</label>
          <input
            type="range"
            min="0.1"
            max="2"
            step="0.01"
            value={params.alpha}
            onChange={(e) =>
              handleChange("alpha", parseFloat(e.target.value))
            }
            className="w-full"
          />
        </div>

        <div>
          <label>Strong Force: {params.strong_force.toFixed(2)}</label>
          <input
            type="range"
            min="0.1"
            max="2"
            step="0.01"
            value={params.strong_force}
            onChange={(e) =>
              handleChange("strong_force", parseFloat(e.target.value))
            }
            className="w-full"
          />
        </div>

        <div>
          <label>Electron Mass: {params.electron_mass.toFixed(2)}</label>
          <input
            type="range"
            min="0.1"
            max="2"
            step="0.01"
            value={params.electron_mass}
            onChange={(e) =>
              handleChange("electron_mass", parseFloat(e.target.value))
            }
            className="w-full"
          />
        </div>
      </div>

      {/* RESULTADO */}
      {loading && <p className="mt-6">Simulating...</p>}

      {result && (
        <div className="mt-6 bg-gray-900 p-4 rounded">
          <p>🌟 Stars: {String(result.star_stability)}</p>
          <p>⚛️ Heavy Elements: {String(result.heavy_elements)}</p>
          <p>🧪 Chemistry: {result.chemistry_score.toFixed(2)}</p>
          <p>🌍 Habitability: {result.habitability_score.toFixed(2)}</p>
          <p className="mt-4 text-gray-300">
            {result.explanation}
          </p>
        </div>
      )}

      {/* MAPA */}
      <h2 className="mt-10 text-xl font-semibold">
        Universe Map
      </h2>

      <UniverseMap data={gridData} currentParams={params} />
    </main>
  );
}