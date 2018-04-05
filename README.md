# simpleci-template-creation

# Docker build Command
docker build -t simpleci-template-creation:0.1 . 
docker-compose build 

# Docker Run command 
docker run -d -p 0.0.0.0:8000:8000 -v /opt:/app/output simpleci-template-creation:0.1
docker-compose up -d 

# Access URL
http://127.0.0.1:8000/
