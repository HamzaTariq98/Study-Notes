FROM node:17-alpine

RUN npm install -g nodemon

WORKDIR /app

# Running package intall to cache modules even if the app contents changed
COPY package.json . 

RUN npm install

COPY . .

EXPOSE 4000

CMD [ "npm","run","dev" ]