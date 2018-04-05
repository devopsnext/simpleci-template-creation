# simpleci-template-creation

# Docker build Command
docker build -t simpleci-template-creation:0.1 . 

# Docker Run command 
docker run -d -p 0.0.0.0:8000:8000 -v /opt:/app/output simpleci-template-creation:0.1

# Access http://127.0.0.1:8000/
