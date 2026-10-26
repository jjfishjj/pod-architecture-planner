"""Capacity planner for NVIDIA BasePOD/SuperPOD-style GPU infrastructure."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class PodPlan:
    gpu_count: int
    gpus_per_node: int
    node_count: int
    estimated_it_kw: float
    recommended_tier: str
    fabric: str
    rack_count: int


def plan(gpu_count: int, gpus_per_node: int = 8, gpu_watts: int = 700, overhead_ratio: float = 0.35) -> PodPlan:
    if gpu_count <= 0 or gpus_per_node <= 0 or gpu_watts <= 0 or overhead_ratio < 0:
        raise ValueError("counts and wattage must be positive; overhead cannot be negative")
    nodes = math.ceil(gpu_count / gpus_per_node)
    it_kw = gpu_count * gpu_watts * (1 + overhead_ratio) / 1000
    tier = "single-node" if nodes == 1 else "BasePOD" if gpu_count <= 128 else "SuperPOD"
    fabric = "NVLink/NVSwitch" if nodes == 1 else "InfiniBand with GPUDirect RDMA"
    racks = math.ceil(nodes / 4)
    return PodPlan(gpu_count, gpus_per_node, nodes, round(it_kw, 2), tier, fabric, racks)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gpus", type=int, required=True)
    parser.add_argument("--gpus-per-node", type=int, default=8)
    parser.add_argument("--gpu-watts", type=int, default=700)
    parser.add_argument("--overhead", type=float, default=0.35)
    args = parser.parse_args()
    print(json.dumps(asdict(plan(args.gpus, args.gpus_per_node, args.gpu_watts, args.overhead)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
