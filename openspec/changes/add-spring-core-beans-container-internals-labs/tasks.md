## 1. Spec & Docs

- [x] 1.1 Update spec delta for beans module (container internals)
- [x] 1.2 Add docs chapters (12+): one chapter per Lab

## 2. Labs (enabled by default)

- [x] 2.1 Add container bootstrap + infrastructure processors Lab
- [x] 2.2 Add BeanDefinitionRegistryPostProcessor Lab
- [x] 2.3 Add BFPP/BPP ordering Lab (PriorityOrdered/Ordered/unordered)
- [x] 2.4 Add pre-instantiation short-circuit Lab (before-instantiation replacement)
- [x] 2.5 Add early reference / circular dependency Lab (early proxy)
- [x] 2.6 Add lifecycle callback order Lab (Aware/BPP/init/destroy)
- [x] 2.7 Add @Lazy (bean vs injection-point) Lab
- [x] 2.8 Add @DependsOn semantics Lab
- [x] 2.9 Add ResolvableDependency Lab
- [x] 2.10 Add parent/child ApplicationContext hierarchy Lab
- [x] 2.11 Add bean name & alias resolution Lab
- [x] 2.12 Add FactoryBean deep-dive Lab (type matching/lookup)
- [x] 2.13 Add BeanDefinition overriding Lab
- [x] 2.14 Add programmatic BeanPostProcessor registration Lab
- [x] 2.15 Add SmartInitializingSingleton Lab
- [x] 2.16 Add SmartLifecycle/phase Lab
- [x] 2.17 Add custom scope + scoped proxy (thread scope) Lab
- [x] 2.18 Add FactoryBean edge cases Lab (getObjectType=null)

## 3. Exercises (disabled by default)

- [x] 3.1 Add custom Scope + scoped proxy exercise
- [x] 3.2 Add SmartLifecycle/phase exercise
- [x] 3.3 Add deeper FactoryBean/metadata edge-cases exercise (optional)

## 4. Navigation updates

- [x] 4.1 Update `spring-core-beans/README.md` reading order + concept map + labs/exercises index
- [x] 4.2 Update root `README.md` to keep beans index short (link-only)

## 5. Verification

- [x] 5.1 Run `mvn -q -pl spring-core-beans test`
- [x] 5.2 Run `mvn -q test`
