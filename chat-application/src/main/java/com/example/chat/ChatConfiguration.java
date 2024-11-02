package com.example.chat;

import com.fasterxml.jackson.annotation.JsonProperty;

import io.dropwizard.core.Configuration;
import jakarta.validation.constraints.NotEmpty;

public class ChatConfiguration extends Configuration {

    @NotEmpty
    private String websocketEndpoint = "/chat"; // Default WebSocket endpoint

    @JsonProperty
    public String getWebsocketEndpoint() {
        return websocketEndpoint;
    }

    @JsonProperty
    public void setWebsocketEndpoint(String websocketEndpoint) {
        this.websocketEndpoint = websocketEndpoint;
    }
}
