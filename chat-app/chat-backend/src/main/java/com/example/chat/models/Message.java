public class Message {
    private String sender;
    private String text;
    private long timestamp;
    
    // Constructors
    public Message() {
    }

    public Message(String sender, String text, long timestamp) {
        this.sender = sender;
        this.text = text;
        this.timestamp = timestamp;
    }

    // Getters and Setters
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }
}
