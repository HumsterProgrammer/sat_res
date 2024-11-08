# SAT

## Условие задачи

Алфавит записи формулы {∧,∨,¬,(,),x,0,1}
Найти: выполнима ли она?

Попробовать метод перебора и метод поиска эквивалентных поддеревьев.
Оценить ассимптотику полученных алгоритмов

## Эквивалентности

```
1∨x = 1
0∨x = x
x∨x = x
x∨¬x = 1
1∧x = x
0∧x = 0
x∧x = x
x∧¬x = 0
x∨(y∧z) = x∨y∧x∨z
x∧(y∨z) = x∧y∨x∧z
```

## Грамматика разбора

```

<S> 		::= <conj> <disj_tail>
<disj_tail>	::= ∨ <conj> <disj_tail> | ε
<conj>		::= <expr> <conj_tail>
<conj_tail>	::= ∧ <expr> <conj_tail> | ε
<expr>		::= <var> | ( <S> ) | ¬ <expr>
<var>		::= x <var_tail>
<var_tail>	::= 0 <var_tail> | 1 <var_tail> | ε

```

> Вроде даже получилось LL(1) 

## Формулировка алгоритма сравнения поддеревьев

## Ассимптотика

Ассимптотика классического алгоритма O(2^n). Для недетерминированной машины Тьюринга эта задача является полиномиальной - NP-полной.
