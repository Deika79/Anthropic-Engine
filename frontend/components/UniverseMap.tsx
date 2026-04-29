"use client";

import { useEffect, useRef } from "react";
import { GridPoint } from "@/lib/api";

type Props = {
  data: GridPoint[];
  currentParams: {
    alpha: number;
    strong_force: number;
  };
};

export default function UniverseMap({ data, currentParams }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  const alphaMin = 0.5;
  const alphaMax = 1.5;
  const strongMin = 0.5;
  const strongMax = 1.5;

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || data.length === 0) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const width = canvas.width;
    const height = canvas.height;

    const imageData = ctx.createImageData(width, height);

    // 🔥 HEATMAP
    for (let px = 0; px < width; px++) {
      for (let py = 0; py < height; py++) {
        const alpha =
          alphaMin + (px / width) * (alphaMax - alphaMin);

        const strong =
          strongMin +
          ((height - py) / height) * (strongMax - strongMin);

        let closest: GridPoint | null = null;
        let minDist = Infinity;

        for (const p of data) {
          const dx = p.alpha - alpha;
          const dy = p.strong_force - strong;
          const dist = dx * dx + dy * dy;

          if (dist < minDist) {
            minDist = dist;
            closest = p;
          }
        }

        // ✅ FIX TYPE ERROR
        const h =
          closest !== null
            ? (closest as GridPoint).habitability
            : 0;

        const r = Math.floor(255 * (1 - h));
        const g = Math.floor(255 * h);
        const b = 80;

        const index = (py * width + px) * 4;

        imageData.data[index] = r;
        imageData.data[index + 1] = g;
        imageData.data[index + 2] = b;
        imageData.data[index + 3] = 255;
      }
    }

    ctx.putImageData(imageData, 0, 0);

    // 📐 Ejes
    ctx.strokeStyle = "#aaa";
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.moveTo(0, height);
    ctx.lineTo(width, height);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, height);
    ctx.stroke();

    ctx.fillStyle = "#ddd";
    ctx.font = "12px sans-serif";

    ctx.fillText("alpha", width - 50, height - 10);

    ctx.save();
    ctx.translate(12, 60);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("strong force", 0, 0);
    ctx.restore();

    // 🔴 Punto actual
    const rawX =
      ((currentParams.alpha - alphaMin) /
        (alphaMax - alphaMin)) *
      width;

    const rawY =
      height -
      ((currentParams.strong_force - strongMin) /
        (strongMax - strongMin)) *
        height;

    const x = Math.max(0, Math.min(width, rawX));
    const y = Math.max(0, Math.min(height, rawY));

    ctx.beginPath();
    ctx.arc(x, y, 6, 0, 2 * Math.PI);
    ctx.fillStyle = "white";
    ctx.fill();

    ctx.strokeStyle = "black";
    ctx.lineWidth = 2;
    ctx.stroke();

  }, [data, currentParams]);

  return (
    <div className="mt-6">
      <canvas
        ref={canvasRef}
        width={400}
        height={400}
        className="border border-gray-700"
      />

      {/* 🎨 Leyenda */}
      <div className="mt-4 flex items-center gap-6 text-sm text-gray-300">
        <div className="flex items-center gap-2">
          <div className="w-4 h-4 bg-red-500"></div>
          <span>Low habitability</span>
        </div>

        <div className="flex items-center gap-2">
          <div className="w-4 h-4 bg-green-500"></div>
          <span>High habitability</span>
        </div>
      </div>
    </div>
  );
}