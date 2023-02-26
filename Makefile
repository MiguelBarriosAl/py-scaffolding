
build:
	docker build -t onna-exercise .

run: build
	docker run --name onna -p 9000:80 -d onna-exercise

test: build
	docker run --name onna --rm onna-exercise /usr/local/bin/python -m pytest /app/tests
