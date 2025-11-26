# Distributed Task Orchestrator (Mini Airflow Clone)
A lightweight, production-ready task orchestration system built with FastAPI. Schedule, execute, and monitor tasks with dependencies, retries, and distributed workers—inspired by Apache Airflow.


## Features
	- Task Execution: Create and run tasks asynchronously with real-time status tracking
	- Scheduling: Schedule tasks with cron-like intervals and automatic retries
	- Distributed Workers: Scale horizontally with Celery and Redis
	- DAG Support: Define task dependencies and workflow pipelines
	- Monitoring: Real-time logs, status updates, and WebSocket notifications
	- Production Ready: PostgreSQL persistence, JWT authentication, Docker deployment

## Prerequisites
	- Python 3.9+
	- Docker & Docker Compose (for production setup)
	- Redis (for distributed workers)
	- PostgreSQL (for production persistence)
