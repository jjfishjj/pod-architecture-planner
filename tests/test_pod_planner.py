import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from pod_planner import plan


class PodPlannerTest(unittest.TestCase):
    def test_rounds_nodes_and_racks(self):
        result = plan(33)
        self.assertEqual(result.node_count, 5)
        self.assertEqual(result.rack_count, 2)
        self.assertEqual(result.recommended_tier, "BasePOD")

    def test_superpod_threshold(self):
        self.assertEqual(plan(256).recommended_tier, "SuperPOD")

    def test_power_estimate(self):
        self.assertEqual(plan(8, gpu_watts=700, overhead_ratio=0.25).estimated_it_kw, 7.0)


if __name__ == "__main__":
    unittest.main()
