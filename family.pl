female(pam).
female(liz).
female(pat).
female(ann).
male(jim).
male(bob).
male(tom).
male(peter).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(bob,peter).
parent(peter,jim).

mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
son(X,Y):- male(X),parent(Y,X).
daughter(X,Y):- female(X),parent(Y,X).
cousin(X,Y) :- father(Z,X),brother(Z,W),father(W,Y).
siblings(X,Y):- parent(Z,X),parent(Z,Y),X\==Y.
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):- parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandfather(X,Z):- father(X,Y),parent(Y,Z).
uncle(X,Z):- brother(X,Y),parent(Y,Z).
