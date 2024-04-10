# Setup Virtual Environment

```python
conda create -n jenkins-env python=3.10 -y
conda activate jenkins-env
pip install -r requirements.txt
pip install .
```

# Test the FASTAPI

```json

{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}


```

# Docker Commands
```
docker build -t loan_pred:v1 .
docker build -t manifoldailearning/cicd:latest . 
docker push manifoldailearning/cicd:latest

docker run -d -it --name modelv1 -p 8005:8005 manifoldailearning/cicd:latest bash

docker exec modelv1 python prediction_model/training_pipeline.py

docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear

docker cp modelv1:/code/src/TestResults.xml .

docker exec -d -w /code modelv1 python main.py

docker exec -d -w /code modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8005


```


docker exec api_1 python src/prediction_model/training_pipeline.py
docker exec api_1 pytest -v --junitxml result.xml
docker cp api_1:/app/result.xml .
docker exec api_1 python api.py

# Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins

sudo apt update
sudo apt install fontconfig openjdk-17-jre
java -version

sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

`
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
`


## Installation of Docker

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

'sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin'


'sudo docker run hello-world'



```
sudo usermod -a -G docker jenkins
sudo usermod -a -G docker $USER

```

## Setup Jenkins with github


additional installations:
1) Build Analysis => JUnit
2) Notifications => Email Extension Template

username = admin
pass = `sudo cat /var/lib/jenkins/secrets/initialAdminPassword`

set up github key
Manage Jenkins => Credentials => (global) => add => Secret Text => setcret(personal Access Github token)


## Hook Configuration in github repo setting

Payload URL => http://3.90.108.20:8080/github-webhook
Content type => JSON

## Configure hook from jenkin side

Manage jenkins => system => GitHub => Add github server => (add premake Credential) => Manage Hooks => Test connections => Save


## Jenkins project
Build steps => Execute Shell

Git => Repo URL
Branch => main
Build trigger => Github trigger

add docker plugin => cloud => new cloud (docker) => host URI =unix:///var/run/docker.sock => add credential to able to push new images to docker hub => user(yr docker username) pass(genrate docker key)

sample code

```
echo 'Build started..'

docker stop $(docker ps -aq) && docker container prune -f
docker image prune -f
docker build -t hamzanaser/ml_api:latest https://github.com/HamzaTariq98/jenkins.git
docker run -d -it --name api_1 -p 8005:8005 hamzanaser/ml_api:latest
docker exec api_1 python src/prediction_model/training_pipeline.py
docker exec -d api_1 python api.py

echo 'Build Successful'
echo $BUILD_NUMBER
```


## setup email notification
settings => add admin email
add SMTP server => smtp.gmail.com
Advanced => username(yr email) pass(email token)
check - Use SSL Use TLS
SMTP port is 465 for gmail




## Sample Pipeline

### 1- Github pull and push to Docker container

Execute shell
```
echo 'Build started..'

docker stop $(docker ps -aq) && docker container prune -f
docker image prune -f
docker build -t hamzanaser/ml_api:latest .
echo 'Build Successful'
echo $BUILD_NUMBER
```
Build / Publish Docker Image
```
hamzanaser/ml_api:latest
```

### 2- Training
Execute shell
```
docker stop $(docker ps -aq) && docker container prune -f
docker run -d -it --name api_1 -p 8005:8005 hamzanaser/ml_api:latest
docker exec api_1 python src/prediction_model/training_pipeline.py

```

### 3- Testing
Execute shell

```
docker exec api_1 pytest -v --junitxml result.xml
docker cp api_1:/app/result.xml .
```

Publish JUnit test result report
```
result.xml
```

### 4- Deploy
Execute shell
```
docker exec -d api_1 python api.py
```


