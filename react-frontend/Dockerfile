# whenever you are running the react inside a docker, run it with the -it flag to avoid the errors.

FROM node:16.3.0-alpine AS development

ENV NODE_ENV development
# Add a work directory
WORKDIR /app
# Cache and Install dependencies
COPY package.json .

COPY package-lock.json .

RUN npm install
# Copy app files
COPY . .
# Expose port
EXPOSE 3000
# Start the app
CMD [ "npm", "start" ]