# 03：key / condition / unless：缓存边界

## 实验入口

- `BootCacheLabTest#conditionPreventsCachingWhenFalse`
- `BootCacheLabTest#unlessPreventsCachingBasedOnResult`

## 你应该观察到什么

- condition：在方法执行前判断，false 时不走缓存（每次都会计算）
- unless：在方法执行后判断，满足条件时不缓存返回值

