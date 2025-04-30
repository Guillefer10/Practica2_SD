package main.java.com.examples.p2.controller;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@Controller
public class SimulationController {

        private final WebClient webClient = WebClient.builder().build();

        @GetMapping("/simulate")
        public String simulate(Model model, String path, String invalid, String name) {
                // File test
                Mono<String> fileMono = webClient.get()
                                .uri("http://localhost:5000/file-test?path={p}", path != null ? path : "data.txt")
                                .accept(MediaType.APPLICATION_JSON)
                                .retrieve()
                                .bodyToMono(String.class)
                                .onErrorResume(e -> Mono.just("{\"error\":\"" + e.getMessage() + "\"}"));

                // DB test
                Mono<String> dbMono = webClient.get()
                                .uri("http://localhost:5000/db-test?invalid={i}", invalid != null ? invalid : "false")
                                .accept(MediaType.APPLICATION_JSON)
                                .retrieve()
                                .bodyToMono(String.class)
                                .onErrorResume(e -> Mono.just("{\"error\":\"" + e.getMessage() + "\"}"));

                // Pokemon test
                Mono<String> pokeMono = webClient.get()
                                .uri("http://localhost:5000/poke-test?name={n}", name != null ? name : "pikachu")
                                .accept(MediaType.APPLICATION_JSON)
                                .retrieve()
                                .bodyToMono(String.class)
                                .onErrorResume(e -> Mono.just("{\"error\":\"" + e.getMessage() + "\"}"));

                // Ejecutamos en paralelo y esperamos
                Mono.zip(fileMono, dbMono, pokeMono)
                                .map(tuple -> {
                                        model.addAttribute("fileResult", tuple.getT1());
                                        model.addAttribute("dbResult", tuple.getT2());
                                        model.addAttribute("pokeResult", tuple.getT3());
                                        return "simulate";
                                }).block();

                return "simulate";
        }
}
