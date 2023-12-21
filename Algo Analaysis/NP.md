NP (NonPolynomial) (nondeterministic polynomial) :
is a complexity class such as time complexity and space complexity but 
is the amount of time it would take for a computer to solve the problem if the computer had unlimited resources



> Deterministic and Non-deterministic Algorithms
- deterministic algorithm: for a given particular input, the computer will always produce the same output going through the same states
- non-deterministic algorithm, for the same input, the compiler may produce different output in different runs. In fact, non-deterministic algorithms can’t solve the problem in polynomial time and can’t determine what is the next step.
- The non-deterministic algorithms can show different behaviors for the same input on different execution and there is a degree of randomness to it.

NP is the set of decision problems solvable in polynomial time by a nondeterministic Turing machine.
NP is the set of decision problems verifiable in polynomial time by a deterministic Turing machine.

There are often general hierarchies of complexity classes; for example, it is known that a number of fundamental time and space complexity classes relate to each other in the following way:
[**L**](https://en.wikipedia.org/wiki/L_(complexity) "L (complexity)")⊆**[NL](https://en.wikipedia.org/wiki/NL_(complexity) "NL (complexity)")**⊆**[P](https://en.wikipedia.org/wiki/P_(complexity) "P (complexity)")**⊆**[NP](https://en.wikipedia.org/wiki/NP_(complexity) "NP (complexity)")**⊆**[PSPACE](https://en.wikipedia.org/wiki/PSPACE "PSPACE")**⊆**[EXPTIME](https://en.wikipedia.org/wiki/EXPTIME "EXPTIME")**⊆**[NEXPTIME](https://en.wikipedia.org/wiki/NEXPTIME "NEXPTIME")**⊆**[EXPSPACE](https://en.wikipedia.org/wiki/EXPSPACE "EXPSPACE")**
