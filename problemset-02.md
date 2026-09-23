# CMPS 6610 Problem Set 02

**Name:**__WILL SILVER WAGMAN

In this assignment we'll work on applying the methods we've learned to
analyze recurrences, and also see their behavior in practice. As with
previous assignments, some of of your answers will go in
`main.py`. Please add your written answers to `answers.md` which you can convert
to a PDF using `convert.sh`. Alternatively, you may scan and upload written answers
to a file named `answers.pdf`. 


1. Prove that $\log n! \in \Theta(n \log n).$

upper bound : for n >= 1,
n! = 1 * 2 * ... * n <= n * n * ... * n =n^n.

log n! <= log(n^n)= n log n.
So log n! <= c * n log n with c = 1 for all n >= 1. and thus log n! ∈ O(n log n).

lower bound:
for n >=2,the integers k with ceiling(n/2) <= k <= n number floor(n/2) + 1 >= n/2, and each satisfies k >= n/2. and dropping the smaller factors (each >= 1) can only shrink the product, so n! >= (n/2)^(n/2).

log n! >= (n/2) log(n/2) = (n/2)(log n-1).
for n >= 4 we have log n >= 2, so log n -1 >= (1/2) log n, giving
log n! >= (n/2)(1/2) log n = (1/4) n log n.
So log n! >= c * n log n with c = 1/4 for all n >= 4. Hence log n! ∈ Ω(n log n).

so since log n! is both O(n log n) and Ω(n log n), log n! ∈Θ(n log n).
 
 
2. Derive asymptotic upper bounds for each recurrence below, using a
   method of your choice.

   my note: i used the master theorem for most of these.
   Master Theorem : T(n) = aT(n/b) + f(n), compare f(n) against n^(log_b a).


  * $T(n)=2T(n/6)+1$


a = 2, b = 6, n^(log_6 2) ≈ n^0.387.
f(n) = 1 =O(n^(0.387 - ε)) for any 0 < ε < 0.387, so it's case 1.
T(n) = Θ(n^(log_6 2)), so T(n)= O(n^(log_6 2)) ≈ O(n^0.387).

  * $T(n)=6T(n/4)+n$

a = 6, b = 4, n^(log_4 6) ≈ n^1.292
f(n) = n = O(n^(1.292 - ε))
this is case 1.
T(n) = O(n^(log_4 6)) ≈O(n^1.292).


  * $T(n)=7T(n/7)+n$


a = 7, b = 7, n^(log_7 7) =n. f(n) = n = Θ(n). it's case 2.
T(n) = O(n log n).


  * $T(n)=9T(n/4)+n^2$
.  
a = 9, b = 4, n^(log_4 9) = n^(log_2 3) ≈ n^1.585.
f(n) = n^2 = Ω(n^(1.585 + ε)) with ε = 0.4.
Regularity: 9(n/4)^2 =(9/16)n^2 <=c n^2 with c = 9/16 < 1. it's case 3.
T(n) = O(n^2).
.  
.  
  * $T(n)=4T(n/2)+n^3$

a=4, b =2, n^(log_2 4) = n^2
f(n) = n^3 = Ω(n^(2 + ε)) with ε =1
regularity: 4(n/2)^3 = (1/2)n^3, c = 1/2 < 1.
this iss case 3
T(n) = O(n^3).


  * $T(n)=49T(n/25)+n^{3/2}\log n$
.  
a = 49, b = 25, n^(log_25 49) = n^(log_5 7) ≈ n^1.209
f(n) = n^1.5 log n = Ω(n^(1.209 + ε)) with ε = 0.29
regularity: 49 (n/25)^(3/2) log(n/25) =(49/125) n^(3/2) log(n/25) <=(49/125) n^(3/2) log n, c = 49/125 <1.
this is case 3.
T(n) = O(n^(3/2) log n).
.  
.  
.  
  * $T(n)=T(n-1)+2$
.  
iterating:
T(n) =2 + 2 + ... +2 (n times) +T(0) =2n + T(0).
T(n) =O(n)
.  
.  
.  
  * $T(n)= T(n-1)+n^c$, with $c\geq 1$
.  
iterating again: T(n) = n^c +(n-1)^c + ... + 1^c + T(0) =sum_{k=1}^{n} k^c + T(0) <= n *n^c +T(0) =n^(c+1) + T(0)
T(n) =O(n^(c+1))


  * $T(n)=T(\sqrt{n})+1$

substitute n = 2^m, so m=log n and sqrt(n)= 2^(m/2). 
let S(m) =T(2^m). Then S(m) = S(m/2) +1.
Here a = 1, b = 2, f(m) = 1 =Θ(m^0) so it's case 2 and S(m)= O(log m)
T(n) =O(log log n)


3. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      two subproblems of one fifth of the input size, recursively
      solving each subproblem, and then combining the solutions in quadratic time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively one subproblems of size $n-1$ and then
      combining the solutions in logarithmic time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into a subproblems of size $n/3$ and a subproblem of size
      $2n/3$, recursively solving each subproblem, and then combining
      the solutions in $O(n^{1.1})$ time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions
    (i.e. the non-recursive quantity).
    Which algorithm would you choose? Why?




alg a
 W(n) = 2W(n/5) + n^2. a = 2, b = 5, n^(log_5 2) ≈ n^0.43
 f(n) = n^2 dominates, regularity 2(n/5)^2 = (2/25)n^2 so it's case 3.
Work =Θ(n^2)
Span: S(n) = S(n/5) + n^2 both subproblems in parallel, so only one appears. this is also case 3. span = Θ(n^2)

alg b
W(n) =W(n-1) + log n.
W(n) = sum_{k=1}^{n} log k =log n! = Θ(n log n)
Work =Θ(n log n). 
only one subproblem so nothing runs in parallel: span = Θ(n log n).

alg c
W(n) = W(n/3) +W(2n/3) +n^1.1. 
recursion tree: level k does ((1/3)^1.1 + (2/3)^1.1)^k * n^1.1 ≈(0.939)^k*n^1.1 work -  geometric series with ratio < 1 so the root dominates.
work = Θ(n^1.1). 
span: longest path follows the 2n/3branch, S(n) =S(2n/3) + n^1.1. this is case 3.
span = Θ(n^1.1)

I would choose algorithm b, because it has teh smallest work and the smallest span since n log n =o(n^1.1). i don't think either of these algorithms has any real parallelism.
















4. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions (i.e.,
    the non-recursive quantity). Which algorithm would you choose? Why?



alg a
W(n) = 5W(n/2) + n. a =5, b =2, n^(log_2 5) ≈n^2.32
f(n) = n =O(n^(2.32-ε)) so it's case 1.
Work = Θ(n^(log_2 5)) ≈Θ(n^2.32).
Span: S(n) = S(n/2)+n ---case 3. 
Span = Θ(n).

alg b
W(n) = 2W(n-1) + 1
W(n) =2^n W(0)+(2^n - 1) =Θ(2^n)
Work = Θ(2^n)
Span: S(n) =S(n-1) +1 = Θ(n)

alg c
W(n) =9W(n/3) + n^2
a = 9, b = 3, n^(log_3 9) =n^2 =f(n) so case 2
Work = Θ(n^2 log n)

Span:
S(n) = S(n/3) + n^2, case 3
Span =Θ(n^2).

i would chooser algorithm C because it has the least work by a polynomial margin (n^2 log n vs n^2.32 vs 2^n) and work is the constraint on any machine with a finite number of processors. alg b doesn't work because exponential work cannot be rescued by parallelism unless you have exponentially many processors. alg a has better span than C (n vs n^2) and more parallelism so alg a would win on a machine with at least about n^0.32 processors where its running time drops to Θ(n) while alg c is stuck at Θ(n^2). otherwise, i would choose C.








5. In Module 2 we discussed two algoriths for integer multiplication. The
  first algorithm was simply a recapitulation of the "grade school"
  algorithm for integer multiplication, while the second was the
  Karatsaba-Ofman algorithm. For this problem, you will use the stub
  functions in `main.py` to implement these two algorithms for integer
  multiplication. Once you've correctly implemented them, test the
  empirical running times across a variety of inputs to test whether
  your code scales in the manner predicted by our analyses of the
  asymptotic work.


.  
.  
.  
.  
.  
