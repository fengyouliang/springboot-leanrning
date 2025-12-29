package com.learning.springboot.bootwebclient;

import org.springframework.web.reactive.function.client.ClientRequest;

final class ClientRequestWithHeader {

    private ClientRequestWithHeader() {
    }

    static ClientRequest addHeader(ClientRequest request, String headerName, String headerValue) {
        return ClientRequest.from(request)
                .header(headerName, headerValue)
                .build();
    }
}

