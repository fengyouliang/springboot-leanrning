package com.learning.springboot.springcoretx;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class TxDemoRunner implements ApplicationRunner {

    private final AccountRepository accountRepository;
    private final AccountService accountService;

    public TxDemoRunner(AccountRepository accountRepository, AccountService accountService) {
        this.accountRepository = accountRepository;
        this.accountService = accountService;
    }

    @Override
    public void run(ApplicationArguments args) {
        System.out.println("== spring-core-tx ==");

        accountRepository.deleteAll();

        try {
            accountService.createTwoAccountsThenFail();
        } catch (IllegalStateException ex) {
            System.out.println("expected exception: " + ex.getMessage());
        }
        System.out.println("after rollback, accountCount=" + accountRepository.count());

        accountService.createTwoAccounts();
        System.out.println("after commit, accountCount=" + accountRepository.count());
    }
}

