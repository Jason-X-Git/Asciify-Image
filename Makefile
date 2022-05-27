build: $(CURDIR)
	docker build -t asciify_service .

service: build
	docker run -it --rm -p 8088:8000 asciify_service:latest

test:
	docker run -it --entrypoint poetry asciify_service:latest run pytest

format:
	black ./