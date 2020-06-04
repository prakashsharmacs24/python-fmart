.PHONY: build build-test test run

VERSION ?= latest


build: 
	docker build -t fmart .

build-test: 
	docker build -t fmart-tests:$(VERSION) -f ./Dockerfile.test .

test: build-test
	docker run -it --rm fmart-tests:$(VERSION)

run: build
	docker run -it --rm fmart
