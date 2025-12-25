package com.learning.springboot.springcoreevents;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class EventsDemoRunner implements ApplicationRunner {

    private final UserRegistrationService userRegistrationService;
    private final InMemoryAuditLog auditLog;

    public EventsDemoRunner(UserRegistrationService userRegistrationService, InMemoryAuditLog auditLog) {
        this.userRegistrationService = userRegistrationService;
        this.auditLog = auditLog;
    }

    @Override
    public void run(ApplicationArguments args) {
        System.out.println("== spring-core-events ==");

        auditLog.clear();
        userRegistrationService.register("Alice");
        System.out.println("auditLog.entries=" + auditLog.entries());
    }
}

