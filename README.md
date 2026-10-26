# POD Architecture Planner

把 GPU 數量轉換為節點、機櫃、IT 功耗、fabric 與單機／BasePOD／SuperPOD 級別的初步建議，另有 GitHub Pages 互動規劃器。

## 執行與測試

```bash
python src/pod_planner.py --gpus 256 --gpus-per-node 8 --gpu-watts 700
python -m unittest discover -s tests -v
```

```bash
docker build -t nvidia-lab/pod .
docker run --rm nvidia-lab/pod --gpus 256
```

輸出為 JSON，適合接到容量規劃表、報價流程或 IaC 產生器。一般 CI 驗證分級、進位與功耗計算，Pages workflow 負責網站部署。

## 使用邊界

這是前期 sizing 工具，不是 NVIDIA 認證設計。採購前仍需以模型平行策略、網路 oversubscription、儲存、checkpoint、SLA、散熱、供電及 NVIDIA／合作夥伴驗證架構校正。

