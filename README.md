# simpleci-template-generation

# Docker build Command
docker build -t simpleci-template-creation:1.0 . 

# Docker Run command 
docker run -d -p 0.0.0.0:8000:8000 -v /opt:/app/output simpleci-template-creation:1.0

# Access http://127.0.0.1:8000/
