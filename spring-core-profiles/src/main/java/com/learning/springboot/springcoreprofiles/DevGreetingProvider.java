package com.learning.springboot.springcoreprofiles;

public class DevGreetingProvider implements GreetingProvider {

    @Override
    public String greeting() {
        return "dev greeting";
    }
}

