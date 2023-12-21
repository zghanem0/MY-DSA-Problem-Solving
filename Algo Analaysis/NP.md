NP (NonPolynomial) (nondeterministic polynomial) :
is a complexity class such as time complexity and space complexity but NP used to classify decision problems
is the amount of time it would take for a computer to solve the problem if the computer had unlimited resources



> Deterministic and Non-deterministic Algorithms
- deterministic algorithm: for a given particular input, the computer will always produce the same output going through the same states
- non-deterministic algorithm, for the same input, the compiler may produce different output in different runs. In fact, non-deterministic algorithms can’t solve the problem in polynomial time and can’t determine what is the next step.
- The non-deterministic algorithms can show different behaviors for the same input on different execution and there is a degree of randomness to it.

NP is the set of decision problems solvable in polynomial time by a nondeterministic Turing machine.
NP is the set of decision problems verifiable in polynomial time by a deterministic Turing machine.



> problem's solution:
- varified
- then solved

> P (Polynomial) vs NP (NonPolynomial) 
P: A yes-or-no problem is in P (Polynomial time) if the answer can be computed in polynomial time.
NP: A yes-or-no problem is in NP (Non-deterministic Polynomial time) if a yes answer can be verified in polynomial time.
Intuitively, we can see that if a problem is in P, then it is in NP. Given a potential answer for a problem in P, we can verify the answer by simply recalculating the answer.

Less obvious, and much more difficult to answer, is whether all problems in NP are in P. Does the fact that we can verify an answer in polynomial time mean that we can compute that answer in polynomial time?

There are a large number of important problems that are known to be NP-complete (basically, if any these problems are proven to be in P, then all NP problems are proven to be in P). If P = NP, then all of these problems will be proven to have an efficient (polynomial time) solution.

Most scientists believe that P!=NP. However, no proof has yet been established for either P = NP or P!=NP.

> There are often general hierarchies of complexity classes; for example, it is known that a number of fundamental time and space complexity classes relate to each other in the following way:
[**L**](https://en.wikipedia.org/wiki/L_(complexity) "L (complexity)")⊆**[NL](https://en.wikipedia.org/wiki/NL_(complexity) "NL (complexity)")**⊆**[P](https://en.wikipedia.org/wiki/P_(complexity) "P (complexity)")**⊆**[NP](https://en.wikipedia.org/wiki/NP_(complexity) "NP (complexity)")**⊆**[PSPACE](https://en.wikipedia.org/wiki/PSPACE "PSPACE")**⊆**[EXPTIME](https://en.wikipedia.org/wiki/EXPTIME "EXPTIME")**⊆**[NEXPTIME](https://en.wikipedia.org/wiki/NEXPTIME "NEXPTIME")**⊆**[EXPSPACE](https://en.wikipedia.org/wiki/EXPSPACE "EXPSPACE")**

