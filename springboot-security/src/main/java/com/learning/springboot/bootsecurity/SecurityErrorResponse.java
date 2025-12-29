package com.learning.springboot.bootsecurity;

public record SecurityErrorResponse(String message, int status, String path) {}

