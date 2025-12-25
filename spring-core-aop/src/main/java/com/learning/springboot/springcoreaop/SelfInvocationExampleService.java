package com.learning.springboot.springcoreaop;

import org.springframework.stereotype.Service;

@Service
public class SelfInvocationExampleService {

    @Traced
    public String outer(String name) {
        return "outer->" + inner(name);
    }

    @Traced
    public String inner(String name) {
        return "inner->" + name;
    }
}

