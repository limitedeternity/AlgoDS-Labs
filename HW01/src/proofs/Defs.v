Require Import Coq.Program.Basics.
Require Import Setoid.
Require Import Classical.
Require Import Arith.
Require Import Lia.

(* Condition constructors *)
Definition ConditionBig
   (Nota : nat -> nat -> (nat -> nat) -> (nat -> nat) -> Prop)
   (f g : nat -> nat) : Prop :=
      exists (c : nat), c > 0 ->
      exists (N : nat), forall (n : nat), N < n ->
         (Nota c n f g).

Definition ConditionTheta
   (Nota : nat -> nat -> nat -> (nat -> nat) -> (nat -> nat) -> Prop)
   (f g : nat -> nat) : Prop :=
      exists (c1 c2 : nat), c1 > 0 /\ c2 > 0 ->
      exists (N : nat), forall (n : nat), N < n ->
         (Nota c1 c2 n f g).

Definition ConditionSmall
   (Nota : nat -> nat -> (nat -> nat) -> (nat -> nat) -> Prop)
   (f g : nat -> nat) : Prop :=
      forall (c : nat), c > 0 ->
      exists (N : nat), forall (n : nat), N < n ->
         (Nota c n f g).

(* Relation constructors *)
Definition NormalRelation (Rel : Type -> Type -> Prop)
   (Nota1 : nat -> nat -> (nat -> nat) -> (nat -> nat) -> Prop)
   (Nota2 : nat -> nat -> (nat -> nat) -> (nat -> nat) -> Prop)
   (c : nat) (n : nat) (f g : nat -> nat) : Prop :=
      (Rel (Nota1 c n f g) (Nota2 c n f g)).

Definition ThetaRelation (Rel : Type -> Type -> Prop)
   (Nota1 : nat -> nat -> nat -> (nat -> nat) -> (nat -> nat) -> Prop)
   (Nota2 : nat -> nat -> nat -> (nat -> nat) -> (nat -> nat) -> Prop)
   (c1 : nat) (c2 : nat) (n : nat) (f g : nat -> nat) : Prop :=
      (Rel (Nota1 c1 c2 n f g) (Nota2 c1 c2 n f g)).

(* Big notation definitions *)
Definition BigO (c : nat) (n : nat) (f g : nat -> nat) : Prop :=
   f n <= c * (g n).

Definition BigOmega (c : nat) (n : nat) (f g : nat -> nat) : Prop :=
   c * (g n) <= f n.

Definition BigTheta (c1 : nat) (c2 : nat) (n : nat) (f g : nat -> nat) : Prop :=
  c1 * (g n) <= f n <= c2 * (g n).

(* Small notation definitions *)
Definition SmallO (c : nat) (n : nat) (f g : nat -> nat) : Prop :=
   f n < c * (g n).

Definition SmallOmega (c : nat) (n : nat) (f g : nat -> nat) : Prop :=
   c * (g n) < f n.

(* ========= *)
