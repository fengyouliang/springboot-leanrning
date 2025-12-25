package com.learning.springboot.springcoreaop;

import org.springframework.stereotype.Service;

@Service
public class TracedBusinessService {

    @Traced
    public String process(String input) {
        return "processed:" + input;
    }
}

