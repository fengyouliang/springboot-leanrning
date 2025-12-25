package com.learning.springboot.springcoreaop;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class AopDemoRunner implements ApplicationRunner {

    private final TracedBusinessService tracedBusinessService;
    private final SelfInvocationExampleService selfInvocationExampleService;
    private final InvocationLog invocationLog;

    public AopDemoRunner(
            TracedBusinessService tracedBusinessService,
            SelfInvocationExampleService selfInvocationExampleService,
            InvocationLog invocationLog
    ) {
        this.tracedBusinessService = tracedBusinessService;
        this.selfInvocationExampleService = selfInvocationExampleService;
        this.invocationLog = invocationLog;
    }

    @Override
    public void run(ApplicationArguments args) {
        System.out.println("== spring-core-aop ==");

        invocationLog.reset();
        tracedBusinessService.process("hello");
        System.out.println("after process(...), invocationCount=" + invocationLog.count());

        invocationLog.reset();
        selfInvocationExampleService.outer("Bob");
        System.out.println("after outer(...), invocationCount=" + invocationLog.count());
        System.out.println("note: inner(...) is not traced when called via self-invocation");
    }
}

