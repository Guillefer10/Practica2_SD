package main.java.com.examples.p2.exception;

import com.example.p2.dto.ErrorDTO;
import org.springframework.dao.DataAccessException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.reactive.function.client.WebClientResponseException;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(DataAccessException.class)
    public ResponseEntity<ErrorDTO> handleDb(DataAccessException ex) {
        ErrorDTO err = new ErrorDTO(500, "Error de acceso a datos");
        return ResponseEntity.status(500).body(err);
    }

    @ExceptionHandler(WebClientResponseException.class)
    public ResponseEntity<ErrorDTO> handleApi(WebClientResponseException ex) {
        ErrorDTO err = new ErrorDTO(ex.getRawStatusCode(), "Error al llamar al servicio externo");
        return ResponseEntity.status(ex.getStatusCode()).body(err);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorDTO> handleAll(Exception ex) {
        ErrorDTO err = new ErrorDTO(500, "Error interno inesperado");
        return ResponseEntity.status(500).body(err);
    }
}
