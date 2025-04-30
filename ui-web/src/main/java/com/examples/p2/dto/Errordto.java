package main.java.com.examples.p2.dto;

import java.time.LocalDateTime;

public class ErrorDTO {
    private LocalDateTime timestamp;
    private int code;
    private String messageUsuario;

    public ErrorDTO(int code, String messageUsuario) {
        this.timestamp = LocalDateTime.now();
        this.code = code;
        this.messageUsuario = messageUsuario;
    }
}
