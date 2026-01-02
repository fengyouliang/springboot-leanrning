package com.learning.springboot.springcoretx;

import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.support.TransactionSynchronizationManager;

@Component
public class TxIntrospectionService {

    @Transactional(readOnly = true)
    public boolean isTransactionActive() {
        return TransactionSynchronizationManager.isActualTransactionActive();
    }
}

