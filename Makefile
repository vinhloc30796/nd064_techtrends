# Build the Dockerfile and tag as techtrends
build:
	docker build -t vinhloc30796/techtrends:latest -t techtrends:latest .

# Run the image in detached, with port 3111 mapped to 7111, named techtrends
run:
	docker run -d -p 7111:3111 --name techtrends techtrends:latest

stop:
	docker stop techtrends
	docker rm -f techtrends