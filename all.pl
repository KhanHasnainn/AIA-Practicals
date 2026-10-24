owns(mary, X) :    cat(X),    white_spots(X). 
loves(X, Y) :    owns(X, Y).

friend(X, Y) :   
likes(X, Y),    
likes(Y, X).

meal(X) :   
food(X).

professor_of(X, Y) :    
teaches(X, C),    
studies(Y, C).

brother(A, B) :    
male(A),   
male(B),    
father(F, A),    
father(F, B),    
A \= B.

mother(X, Y) :    parent(X, Y),    female(X). father(X, Y) :    parent(X, Y),    male(X).

sister(X, Y) :    parent(Z, X),    parent(Z, Y),    female(X),    X \= Y.
