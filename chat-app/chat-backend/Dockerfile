FROM openjdk:17-jdk-slim

WORKDIR /app

# Use the shaded jar (note the "-shaded" suffix)
COPY chat-app/chat-backend/target/chat-application-1.0-SNAPSHOT-shaded.jar app.jar
COPY chat-app/chat-backend/config.yml config.yml

EXPOSE 8080
EXPOSE 8081

ENTRYPOINT ["java", "-jar", "app.jar", "server", "config.yml"]