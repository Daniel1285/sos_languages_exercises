% 1
married(leo, emma).
married(alex, grace).
married(liam, ava).
married(hugo, isabella).
married(noah, lily).


male(leo).
male(alex).
male(liam).
male(hugo).
male(ethan).
male(noah).
male(james).

female(emma).
female(luna).
female(lily).
female(grace).
female(ava).
female(isabella).
female(zoe).
female(ella).

parent(leo, lily).
parent(lily, james).
parent(leo, liam).
parent(emma, liam).
parent(leo, ethan).
parent(emma, ethan).
parent(alex, ava).
parent(grace, ava).
parent(liam, hugo).
parent(liam, luna).
parent(ava, hugo).
parent(liam, isabella).
parent(ava, isabella).
parent(james, zoe).
parent(hugo, ella).

% Family relationship predicates
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
son(X, Y) :- parent(Y, X), male(X).
daughter(X, Y) :- parent(Y, X), female(X).

% Grandparent relationships for grandchildren
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandfather(X, Y) :- grandparent(X, Y), male(X).
grandmother(X, Y) :- grandparent(X, Y), female(X).

% Grandchild relationships
grandson(X, Y) :- grandparent(Y, X), male(X).
granddaughter(X, Y) :- grandparent(Y, X), female(X).

% Sibling relationships
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Extended family relationships
uncle(X, Y) :- male(X), parent(Z, Y), married(X, W), sibling(Z, W).
niece(X, Y) :- female(X), sibling(Y, Z), parent(Z, X).
cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2), female(P2), male(Y), X \= Y.

% In-law and other relationships
brother_in_law(X, Y) :- male(X), (married(Z, Y), sibling(X, Z)); (married(Z, X), sibling(Y, Z)).
second_cousin(X, Y) :- parent(A, X), parent(B, Y), cousin(A, B).

% 2

% 2.1 Reverse a list
reverse([], []).
reverse([Head|Tail], Reversed) :-
    reverse(Tail, ReversedTail),
    append(ReversedTail, [Head], Reversed).

% 2.2 Check membership
member(Element, [Element|_]).
member(Element, [_|Tail]) :-
    member(Element, Tail).

% 2.3 Check for palindrome
palindrome(List) :-
    reverse(List, List).

% 2.4 Check if sorted
sorted([]).
sorted([_]).
sorted([First, Second | Tail]) :-
    First =< Second,
    sorted([Second | Tail]).

% 2.5 Generate permutations
permutation([], []).
permutation(List, [Head|Tail]) :-
    select(Head, List, Rest),
    permutation(Rest, Tail).

% 3

%3.1.1
scum(N, Res) :-
    N > 1,
    Sum is (N * (N + 1)) // 2,  % Using the formula for the sum of the first N natural numbers
    Res is Sum.
%3.1.2
sumDigits(Num, Sum) :-
    Num > 0,
    num_to_digits(Num, Digits),
    sum_list(Digits, Sum).

num_to_digits(0, []).
num_to_digits(Num, [Digit | Digits]) :-
    Num > 0,
    Digit is Num mod 10,
    NewNum is Num // 10,
    num_to_digits(NewNum, Digits).


%3.2.1
split(N, Res) :-
    N >= 0,
    num_to_digits1(N, [], Res).

num_to_digits1(0, Acc, Acc) :- !.  % When N is 0, unify the accumulated list with Res.
num_to_digits1(N, Acc, Res) :-
    N > 0,
    Digit is N mod 10,
    NewN is N // 10,
    num_to_digits1(NewN, [Digit | Acc], Res).  % Accumulate in reverse order.

% To reverse the accumulated list to get the correct order
reverse_list([], Acc, Acc).
reverse_list([H|T], Acc, Res) :-
    reverse_list(T, [H|Acc], Res).

split1(N, Res) :-
    N >= 0,
    num_to_digits1(N, [], Acc),
    reverse_list(Acc, [], Res).

%3.2.2
create(List, N) :-
    reverse(List, ReversedList),  % Reverse to get correct positional value
    digits_to_num(ReversedList, N).

digits_to_num([], 0).
digits_to_num([H | T], N) :-
    digits_to_num(T, RestNum),
    length(T, Length),
    Power is 10 ** Length,
    N is H * Power + RestNum.
%3.2.3
reverse_number(N, Reversed) :-
    split(N, Digits),              % Split N into digits
    reverse(Digits, ReversedDigits), % Reverse the list of digits
    digits_to_num2(ReversedDigits, Reversed). % Create a number from the reversed digits.

% This predicate converts a list of digits into a number
digits_to_num2([], 0).  % Base case: empty list results in 0
digits_to_num2([H | T], N) :-
    digits_to_num2(T, RestNum),  % Get the number from the rest of the list
    length(T, Length),           % Find the length of the rest list
    Power is 10 ** Length,       % Calculate the positional value of the head
    N is H * Power + RestNum.    % Combine the head and the rest into the final number

%3.3.1
intersection([], _, []).
intersection([H | T], L2, [H | Res]) :-
    member(H, L2),
    intersection(T, L2, Res).
intersection([H | T], L2, Res) :-
    \+ member(H, L2),
    intersection(T, L2, Res).
%3.3.2
minus([], _, []).
minus([H | T], L2, [H | Res]) :-
    \+ member(H, L2),
    minus(T, L2, Res).
minus([H | T], L2, Res) :-
    member(H, L2),
    minus(T, L2, Res).
