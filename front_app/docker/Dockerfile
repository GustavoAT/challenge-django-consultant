FROM node:20-alpine

WORKDIR /app

COPY ./loan .

RUN npm run build

CMD ["npm", "start"]