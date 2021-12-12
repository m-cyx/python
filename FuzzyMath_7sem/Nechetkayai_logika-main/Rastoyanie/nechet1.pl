max(X,Y,X):-X>Y,!.
max(_,Y,Y).
max(X,Y,Z,R):-max(Y,Z,K),max(X,K,R).
max(A,B,C,D,E,F,G,Res):- max(A,B,C,R1),max(D,E,F,R2), max(R1,R2,G,Res).

min(X,Y,X):-X<Y,!.
min(_,Y,Y).
min(A,B,C,R):-min(A,B,R1), min(R1,C,R).

write_str([]):-!.
write_str([H|T]):-put(H),write_str(T).
write_list_str([]):-!.
write_list_str([H|T]):-write_str(H),nl,write_list_str(T).
%istomin_nike@mail.ru
frontchar([H|T],H, T).




ne_hod(X,Y):-X=0,Y is 0.

chasto(X,Y,A,Sygma):-0=<X, X=<2*(A - Sygma), Y is 1-0.5*X/(A - Sygma),!.
chasto(X,Y,A,Sygma):-X>2*(A - Sygma), Y is 0.

normal(X,Y,A,Sygma):- X < (A - Sygma / 0.5), Y is 0,!.
normal(X,Y,A,Sygma):-(A - 2 * Sygma)=<X, X=<A, Y is 0.5 / Sygma * (X - A) + 1,!.
normal(X,Y,A,Sygma):-A<X, X=<A + 2* Sygma, Y is - 0.5 / Sygma * (X - A) + 1,!.
normal(X,Y,A,Sygma):-X > A + 2* Sygma, Y is 0.

redko(X,Y,A,Sygma):-X<A, Y is 0,!.
redko(X,Y,A,Sygma):-A=<X, X=<A + 2 * Sygma, Y is (X - A) / 2 / Sygma,!.
redko(X,Y,A,Sygma):-A + 2 * Sygma <X, Y is 1,!.




small(X,Y,A,Sygma):-0=<X, X=<2*(A-Sygma), Y is 1 - 0.5*X/(A-2*Sygma),!.
small(X,Y,A,Sygma):-X>2*(A-Sygma),  Y is 0,!.

middle(X,Y,A,Sygma):-X<A-3*Sygma, Y is 0,!.
middle(X,Y,A,Sygma):-A-3*Sygma=<X, X=<A-Sygma, Y is (X-A)/(2*Sygma)+1.5,!.
middle(X,Y,A,Sygma):-A-Sygma=<X, X=<A+Sygma, Y is (-X + A)/(2*Sygma)+0.5,!.
middle(X,Y,A,Sygma):-X>A+Sygma, Y is 0.

ne_large(X,Y,A,Sygma):-X<A-Sygma, Y is 0,!.
ne_large(X,Y,A,Sygma):-A-Sygma=<X, X=<A+Sygma, Y is (X-A)/(2*Sygma)+0.5,!.
ne_large(X,Y,A,Sygma):-A+Sygma=<X, X=<A+3*Sygma, Y is (-X + A)/(2*Sygma)+1.5,!.
ne_large(X,Y,A,Sygma):- A+3*Sygma>89,  Y is 0.

large(X,Y,A,Sygma):-X<A+Sygma, Y is 0,!.
large(X,Y,A,Sygma):-A+Sygma=<X, X=<A+3*Sygma, Y is (X-A)/(2*Sygma)-0.5,!.
large(X,Y,A,Sygma):-A+3*Sygma=<X, Y is 1.



morning(X,Y,A,Sygma):-0=<X, X=<2*(A-Sygma), Y is 1 - 0.5*X/(A-2*Sygma),!.
morning(X,Y,A,Sygma):-X>2*(A-Sygma),  Y is 0,!.

dinner(X,Y,A,Sygma):-X<A-3*Sygma, Y is 0,!.
dinner(X,Y,A,Sygma):-A-3*Sygma=<X, X=<A-Sygma, Y is (X-A)/(2*Sygma)+1.5,!.
dinner(X,Y,A,Sygma):-A-Sygma=<X, X=<A+Sygma, Y is (-X + A)/(2*Sygma)+0.5,!.
dinner(X,Y,A,Sygma):-X>A+Sygma, Y is 0.

evenning(X,Y,A,Sygma):-X<A-Sygma, Y is 0,!.
evenning(X,Y,A,Sygma):-A-Sygma=<X, X=<A+Sygma, Y is (X-A)/(2*Sygma)+0.5,!.
evenning(X,Y,A,Sygma):-A+Sygma=<X, X=<A+3*Sygma, Y is (-X + A)/(2*Sygma)+1.5,!.
evenning(X,Y,A,Sygma):- A+3*Sygma>89,  Y is 0.

night(X,Y,A,Sygma):-X<A+Sygma, Y is 0,!.
night(X,Y,A,Sygma):-A+Sygma=<X, X=<A+3*Sygma, Y is (X-A)/(2*Sygma)-0.5,!.
night(X,Y,A,Sygma):-A+3*Sygma=<X, Y is 1.

/*
morning(X,Y,A,Sygma):-0=<X, X=<12, Y is 1-(X*X / 144),!.
morning(X,Y,A,Sygma):-X>12, Y is 0.

dinner(X,Y,A,Sygma):-X<10, Y is 0,!.
dinner(X,Y,A,Sygma):-10=<X, X=<12, Y is (X / 2)-5,!.
dinner(X,Y,A,Sygma):-12<X, X=<16, Y is 1,!.
dinner(X,Y,A,Sygma):-16<X, X=<18, Y is 7-(X / 2),!.
dinner(X,Y),A,Sygma:-X>18, Y is 0.

evenning(X,Y,A,Sygma):-X<16, Y is 0,!.
evenning(X,Y,A,Sygma):-16=<X, X=<22, Y is -(X*X / 9)+(38*X / 9)-(352 / 9),!.
evenning(X,Y,A,Sygma):- X>22, Y is 0,!.

night(X,Y,A,Sygma):-X<20, Y is 0,!.
night(X,Y,A,Sygma):-20=<X, X=<22, Y is (X / 2)-10,!.
night(X,Y,A,Sygma):-22 < X, Y is 1.
*/


peshok(X,Y):-0=<X, X=<1, Y is -X +1,!.
peshok(X,Y):-X>1, Y is 0.

obsch(X,Y):-0=<X, X=<1, Y is X,!.
obsch(X,Y):-1<X, X=<2, Y is -X+2,!.
obsch(X,Y):-X>2, Y is 0.

car(X,Y):-X<1, Y is 0,!.
car(X,Y):- 1=<X, X=<2, Y is X-1,!.
car(X,Y):- 2<X, X=<3, Y is -X+3,!.
car(X,Y):-X>3, Y is 0.

obsch_peh(X,Y):-X<2, Y is 0,!.
obsch_peh(X,Y):- 2=<X, X=<3, Y is X-2,!.
obsch_peh(X,Y):- 3<X, X=<4, Y is -X+4,!.
obsch_peh(X,Y):-X>4, Y is 0.

car_peh(X,Y):-X<3, Y is 0,!.
car_peh(X,Y):- 3=<X, X=<4, Y is X-3,!.
car_peh(X,Y):- 4<X, X=<5, Y is -X+5,!.
car_peh(X,Y):-X>5, Y is 0.

obsch_car(X,Y):- X<4, Y is 0,!.
obsch_car(X,Y):- 4=<X, X=<5, Y is X-4,!.
obsch_car(X,Y):- 5<X, Y is 1.



otvet(Fchislo,Flist):-0=<Fchislo, Fchislo<0.5,string_codes("1Пешком",Flist), write_str(Flist).
otvet(Fchislo,Flist):-0.5=<Fchislo, Fchislo<1.5,string_codes("2Общественным транспортом",Flist), write_str(Flist).
otvet(Fchislo,Flist):-1.5=<Fchislo, Fchislo<2.5,string_codes("3Машиной",Flist), write_str(Flist).
otvet(Fchislo,Flist):-2.5=<Fchislo, Fchislo<3.5,string_codes("4Пересадкой с ног на общественный",Flist), write_str(Flist).
otvet(Fchislo,Flist):-3.5=<Fchislo, Fchislo<4.5,string_codes("5Пересадкой с ног на машину",Flist), write_str(Flist).
otvet(Fchislo,Flist):-4.5=<Fchislo,string_codes("6Общественным с пересадкой на машину",Flist), write_str(Flist).


pr(S,T,Tr,A1,Sygma1,A2,Sygma2,A3,Sygma3,Fchislo) :- defuzy(S,T,Tr,Fchislo,A1,Sygma1,A2,Sygma2,A3,Sygma3).

defuzy(S,T,Tr, Fchislo,A1,Sygma1,A2,Sygma2,A3,Sygma3) :- defuzy(0,0,0,Sum1,Sum2,S,T,Tr,A1,Sygma1,A2,Sygma2,A3,Sygma3),
                                                        (Sum2>0, Fchislo is Sum1 / Sum2,! ; Fchislo is 0).
%пройтись в цикле, найти sum1, sum2
%получить F-число,а потом F

defuzy(X,Sum1,Sum2,Sum1,Sum2,_,_,_,A1,Sygma1,A2,Sygma2,A3,Sygma3):-X>6,!.
defuzy(X,CurrentSum1,CurrentSum2,Sum1,Sum2,S,T,Tr,A1,Sygma1,A2,Sygma2,A3,Sygma3):-
     funcmu(X,FuncMu,S,T,Tr,A1,Sygma1,A2,Sygma2,A3,Sygma3),
     NewSum1 is CurrentSum1 + FuncMu * X,
     NewSum2 is CurrentSum2 + FuncMu,
     X1 is X + 0.1,
     defuzy(X1,NewSum1,NewSum2,Sum1,Sum2,S,T,Tr,A1,Sygma1,A2,Sygma2,A3,Sygma3).


funcmu(X,FuncMu,S,T,Tr,A1,Sygma1,A2,Sygma2,A3,Sygma3):-
     rul1(S,T,X,R1,A1,Sygma1,A2,Sygma2),
     rul2(T,X,R2,A2,Sygma2),
     rul3(S,T,Tr,X,R3,A1,Sygma1,A2,Sygma2,A3,Sygma3),
     rul4(S,T,Tr,X,R4,A1,Sygma1,A2,Sygma2,A3,Sygma3),
     rul5(S,T,Tr,X,R5,A1,Sygma1,A2,Sygma2,A3,Sygma3),
     rul6(S,T,Tr,X,R6,A1,Sygma1,A2,Sygma2,A3,Sygma3),
     rul7(S,T,X,R7,A1,Sygma1,A2,Sygma2),
     max(R1,R2,R3,R4,R5,R6,R7,FuncMu).



rul1(S,T,X,R1,A1,Sygma1,A2,Sygma2) :- vhodi1(S,T,Result,A1,Sygma1,A2,Sygma2),peshok(X,Y), min(Result,Y,R1).
vhodi1(S,T,Result,A1,Sygma1,A2,Sygma2):- small(S,Y1,A1,Sygma1), morning(T,T_Y1,A2,Sygma2), evenning(T,T_Y2,A2,Sygma2),
     max(T_Y1,T_Y2, Y2), min(Y1,Y2,Result).

rul2(T,X,R2,A2,Sygma2):-vhodi2(T,Result,A2,Sygma2),car(X,Y),min(Result,Y,R2).
vhodi2(T,Result,A2,Sygma2):- night(T,Result,A2,Sygma2).


rul3(S,T,Tr,X,R3,A1,Sygma1,A2,Sygma2,A3,Sygma3):-vhodi3(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3),car_peh(X,Y),min(Result,Y,R3).

mid_morn_ev(S,T,Result,A1,Sygma1,A2,Sygma2):-middle(S,Y1,A1,Sygma1),
                                            morning(T,T_Y1,A2,Sygma2),
                                            evenning(T,T_Y2,A2,Sygma2),
                                            max(T_Y1,T_Y2, Y2), min(Y1,Y2,Result).
mid_din_chas(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3):- middle(S,Y1,A1,Sygma1),
                                                          dinner(T,Y2,A2,Sygma2),
                                                          chasto(Tr,Y3,A3,Sygma3),
                                                          min(Y1,Y2,Y3,Result).
vhodi3(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3):- mid_morn_ev(S,T,R1,A1,Sygma1,A2,Sygma2),
                                                        mid_din_chas(S,T,Tr,R2,A1,Sygma1,A2,Sygma2,A3,Sygma3),
                                                        min(R1,R2,Result).

rul4(S,T,Tr,X,R4,A1,Sygma1,A2,Sygma2,A3,Sygma3):- vhodi4(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3),obsch_car(X,Y),min(Result,Y,R4).
vhodi4(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3):- middle(S,Y1,A1,Sygma1),
                                                        dinner(T,Y2,A2,Sygma2),
                                                        chasto(Tr,Tr_Y1,A3,Sygma3),
                                                        normal(Tr,Tr_Y2,A3,Sygma3),
                                                        max(Tr_Y1,Tr_Y2,Y3),min(Y1,Y2,Y3,Result).

rul5(S,T,Tr,X,R5,A1,Sygma1,A2,Sygma2,A3,Sygma3):-vhodi5(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3),peshok(X,Y1),obsch(X,Y2),max(Y1,Y2,Y),min(Result,Y,R5).
vhodi5(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3):-small(S,Y1,A1,Sygma1),
                                                        dinner(T,Y2,A2,Sygma2),
                                                        chasto(Tr,Y3,A3,Sygma3),
                                                        min(Y1,Y2,Y3,Result).

rul6(S,T,Tr,X,R6,A1,Sygma1,A2,Sygma2,A3,Sygma3):-vhodi6(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3),peshok(X,Y1),car(X,Y2),max(Y1,Y2,Y),min(Result,Y,R6).
vhodi6(S,T,Tr,Result,A1,Sygma1,A2,Sygma2,A3,Sygma3):-small(S,Y1,A1,Sygma1),
                                                     dinner(T,Y2,A2,Sygma2),
                                                     normal(Tr,Tr_Y1,A3,Sygma3),
                                                     redko(Tr,Tr_Y2,A3,Sygma3),
                                                     max(Tr_Y1,Tr_Y2,Y3),
                                                     min(Y1,Y2,Y3,Result).

rul7(S,T,X,R7,A1,Sygma1,A2,Sygma2):-vhodi7(S,T,Result,A1,Sygma1,A2,Sygma2),obsch(X,Y1),car(X,Y2),max(Y1,Y2,Y),min(Result,Y,R7).
vhodi7(S,T,Result,A1,Sygma1,A2,Sygma2):-large(S,S_Y1,A1,Sygma1),ne_large(S,S_Y2,A1,Sygma1),max(S_Y1,S_Y2,Y1),
                                        morning(T,T_Y1,A2,Sygma2),dinner(T,T_Y2,A2,Sygma2),evenning(T,T_Y3,A2,Sygma2),max(T_Y1,T_Y2,T_Y3,Y2),
                                        min(Y1,Y2,Result).