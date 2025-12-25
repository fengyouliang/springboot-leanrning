package com.learning.springboot.springcoreprofiles;

public class FancyGreetingProvider implements GreetingProvider {

    @Override
    public String greeting() {
        return "fancy greeting";
    }
}

