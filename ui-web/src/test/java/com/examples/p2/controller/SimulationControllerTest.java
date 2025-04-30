package test.java.com.examples.p2.controller;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.autoconfigure.web.reactive.WebFluxTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.web.reactive.server.WebTestClient;

@WebFluxTest(SimulationController.class)
public class SimulationControllerTest {

    @Autowired
    private WebTestClient client;

    @Test
    void simulateDefault() {
        client.get().uri("/simulate")
                .exchange()
                .expectStatus().isOk()
                .expectBody(String.class)
                .consumeWith(resp -> {
                    String body = resp.getResponseBody();
                    assert body != null && body.contains("Simulación de Excepciones");
                });
    }
}
