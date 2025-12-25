package com.learning.springboot.springcoreevents;

import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

@Component
public class UserRegisteredListener {

    private final InMemoryAuditLog auditLog;

    public UserRegisteredListener(InMemoryAuditLog auditLog) {
        this.auditLog = auditLog;
    }

    @EventListener
    public void onUserRegistered(UserRegisteredEvent event) {
        String entry = "userRegistered:" + event.username();
        auditLog.add(entry);
        System.out.println("EventListener received: " + entry);
    }
}

