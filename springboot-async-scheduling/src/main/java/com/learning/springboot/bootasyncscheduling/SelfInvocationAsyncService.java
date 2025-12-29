package com.learning.springboot.bootasyncscheduling;

import java.util.concurrent.CompletableFuture;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
class SelfInvocationAsyncService {

    CompletableFuture<String> outerCallsAsyncMethod() {
        return asyncMethod();
    }

    @Async
    CompletableFuture<String> asyncMethod() {
        return CompletableFuture.completedFuture(Thread.currentThread().getName());
    }
}

