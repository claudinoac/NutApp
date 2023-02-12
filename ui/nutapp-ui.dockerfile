FROM node:14-alpine
COPY ./package.json ./yarn.lock  /code/
WORKDIR /code/
RUN npm install yarn
RUN yarn install --update-lockfile --update-checksums
COPY . /code/
CMD yarn serve
