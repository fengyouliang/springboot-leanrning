package com.learning.springboot.bootsecurity;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/jwt/public")
class JwtPublicController {

    @GetMapping("/ping")
    MessageResponse ping() {
        return new MessageResponse("pong_jwt_public");
    }
}

