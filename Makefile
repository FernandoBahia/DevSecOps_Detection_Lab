.PHONY: test validate docker-test detect clean

test:
	python -m python.runner

validate:
	sigma check detections/sigma/*.yml

docker-test:
	docker compose -f docker/docker-compose.yml run --rm detection-lab

detect:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make detect FILE=telemetry/samples/<file>.json"; \
		exit 1; \
	fi
	python -m python.engine.detection_engine $(FILE)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
