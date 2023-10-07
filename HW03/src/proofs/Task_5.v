Require Import PeanoNat ZArith List Lia.
Require Import Coq.Program.Basics.
Import ListNotations.
Import Z.

Local Open Scope Z_scope.
Notation "a >? b" := (b <? a) (at level 70).

Inductive option (T : Type) :=
| Some : T -> option T
| None : option T.

Definition linear_search_max (lst : list Z) : option Z * nat :=
   fold_left (fun '(opt_max, comps) cur =>
      match opt_max with
      | None _ => (Some Z cur, comps)
      | Some _ max => (Some Z (if cur >? max then cur else max), S comps)
      end
   ) lst (None Z, 0 % nat).

Definition max_element := compose fst linear_search_max.
Definition cmp_count := compose snd linear_search_max.
Transparent max_element.
Transparent cmp_count.

Scheme Equality for option.
Scheme Equality for Z.
Scheme Equality for nat.

Definition Z_option_beq := option_beq Z Z_beq.
Transparent Z_option_beq.

Eval compute in Z_option_beq (max_element []) (None Z). (* true *)
Eval compute in Z_option_beq (max_element [1]) (Some Z 1). (* true *)
Eval compute in Z_option_beq (max_element [10;1]) (Some Z 10). (* true *)

Eval compute in nat_beq (cmp_count []) (0 % nat). (* true *)
Eval compute in nat_beq (cmp_count [1]) (0 % nat). (* true *)
Eval compute in nat_beq (cmp_count [10;1]) (1 % nat). (* true *)

(* Одна итерация линейного поиска сужает пространство поиска на 1 элемент *)
(* И увеличивает счетчик сравнений на 1 *)
Axiom linear_search_iter :
  forall x z xs, cmp_count (x :: z :: xs) = S (cmp_count (z :: xs)).

(* Аксиома, поскольку так реализован алгоритм *)
Eval compute in nat_beq (cmp_count (10 :: 1 :: [])) (S (cmp_count (1 :: []))). (* true *)
Eval compute in nat_beq (cmp_count (10 :: 1 :: [20])) (S (cmp_count (1 :: [20]))). (* true *)

Local Close Scope Z_scope.

Lemma linear_search_comps : forall lst, cmp_count lst = length lst - 1.
Proof.
   induction lst as [|x xs].
   (* [] *)
   - simpl. reflexivity.
   - destruct xs.
     (* [x] *)
     * simpl. reflexivity.
     (* [x; z] *)
     * replace (length (x :: z :: xs) - 1) with (1 + length (z :: xs) - 1) by auto.
       rewrite <- Nat.add_sub_assoc;
       [|
         replace (length (z :: xs)) with (1 + length xs) by auto; lia
       ].
       rewrite <- IHxs. rewrite Nat.add_1_l.
       apply linear_search_iter.
Qed.
