# Build stage
FROM node:14 as build

WORKDIR /app

# Copy package files
COPY chat-app/chat-frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY chat-app/chat-frontend/ ./

# Build the application
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy build files from build stage
COPY --from=build /app/build /usr/share/nginx/html

# Copy nginx configuration if you have custom config
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]