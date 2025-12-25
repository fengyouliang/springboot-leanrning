package com.learning.springboot.springcoreprofiles;

public class DefaultGreetingProvider implements GreetingProvider {

    @Override
    public String greeting() {
        return "default greeting";
    }
}

