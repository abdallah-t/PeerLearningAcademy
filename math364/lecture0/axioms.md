# Axioms

## introduction

The most important question in math is 'why?'. asking why is the key to understanding math. But how far can we ask why? we can't ask why about everything. We have to stop at some point. We have to stop at some statements that we assume to be true without proof. These statements are called axioms.

## what is an axiom?

An axiom is a statement that is assumed to be true without proof. Axioms are the building blocks of mathematics. They are used to prove theorems. Axioms are also called postulates.

Axioms are different depending on the field of math. but for this course we will use the Field Axioms.

## Field Axioms

- ### addition commutativity

    `a + b = b + a`

- ### addition associativity

    `(a + b) + c = a + (b + c)`

- ### additive identity

    `a + 0 = a`

- ### additive inverse

    `a + (-a) = 0`

- ### multiplication commutativity

    `a * b = b * a`

- ### multiplication commutativity

    `(a * b) * c = a * (b * c)`

- ### multiplicative identity

    `a * 1 = a`

- ### multiplicative inverse

    `a * (1/a) = 1` if `a != 0`

- ### multiplication distributes over addition

    `a * (b + c) = (a * b) + (a * c)`

- ### trichotomy law

    $\forall a \in \mathbb{R}, a > 0 \lor a = 0 \lor a < 0$

- ### positive numbers are closed under addition and multiplication

    if `a > 0` and `b > 0` then `a + b > 0` and `a * b > 0`

- ### least upper bound axiom

    $\forall S \subseteq \mathbb{R}, S \neq \emptyset, S \neq \mathbb{R}, S \subseteq \mathbb{R}^+, \exists b \in \mathbb{R}, \forall x \in S, x \leq b$

anything that is not an axiom is called a theorem. and theorems are proved using axioms. even the most basic theorems like

- `a * 0 = 0`
- `a * (-b) = -(a * b)`
- `a * b = 0` if `a = 0` or `b = 0`
- `a * b = a * c` if `a != 0` and `b = c`
- etc...

## why am I showing you these axioms?

Because axioms would make you understand the things that you've always struggled to understand. For example, one time in 8th grade I asked my teacher why is if `a + x = b + x` then `a = b`? and he told me we can cancel `x` on each side of the equation. I asked him why? and he didn't give a valid answer and acted like I'm stupid for asking. But now I know why. Do you know why?

I know it makes sense. but we need to proof it. so lets go ahead and prove it.

### proof
