FROM python:3.12-slim
WORKDIR /workspace
COPY src/ src/
ENTRYPOINT ["python", "src/pod_planner.py"]
