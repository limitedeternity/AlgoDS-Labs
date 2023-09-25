Require Import ZArith List Lia.
Import ListNotations.
Import Z.
Local Open Scope Z_scope.

Fixpoint total (lst : list Z) : Z :=
   match lst with
   | [] => 0
   | x :: xs => x + total xs
   end.

Definition Sublist (lst1 lst2 : list Z) : Prop :=
   exists pre suf, lst2 = pre ++ lst1 ++ suf.

Definition Prefix (lst1 lst2 : list Z) : Prop :=
   exists suf, lst2 = lst1 ++ suf.

Definition Max_sub_sum (lst1 lst2 : list Z) : Prop :=
   Sublist lst1 lst2 /\ (forall sub, Sublist sub lst2 -> total sub <= total lst1).

Definition Max_pre_sum (lst1 lst2 : list Z) : Prop :=
   Prefix lst1 lst2 /\ (forall pre, Prefix pre lst2 -> total pre <= total lst1).

Fixpoint max_sub_sum_aux (lst : list Z) : Z * Z :=
   match lst with
   | [] => (0, 0)
   | x :: xs =>
      let (p, q) := max_sub_sum_aux xs in
         (max 0 (x + p), max (x + p) q)
   end.

Definition max_sub_sum (lst : list Z) : Z := snd (max_sub_sum_aux lst).
Eval compute in max_sub_sum [1; 2; -5; 3; 2; -1; 5; -10; 3; 2]. (* 9 *)
Eval compute in max_sub_sum [-2; 1; -3; 4; -1; 2; 1; -5; 4]. (* 6 *)

Definition max_list (lst1 lst2 : list Z) : list Z :=
   if max_dec (total lst1) (total lst2) then lst1 else lst2.

Theorem total_max_list : forall lst1 lst2,
   total (max_list lst1 lst2) = max (total lst1) (total lst2).
Proof.
   intros.
   unfold max_list.
   now destruct max_dec.
Qed.

Theorem max_sub_sum_aux_correct : forall (lst : list Z),
  exists s1 s2, Max_pre_sum s1 lst /\ Max_sub_sum s2 lst /\ (total s1, total s2) = max_sub_sum_aux lst.
Proof.
  induction lst as [|x xs].
  - exists [], []. repeat split.
    + now exists [].
    + intros b [suf Hb]. now destruct b.
    + now exists [], [].
    + intros b [pre [suf Hb]]. now destruct b,pre.
  - destruct IHxs as [s1 [s2 [Hs1 [Hs2 IH]]]].
    cbn. rewrite <- IH.
    exists (max_list [] (x :: s1)), (max_list (x :: s1) s2).
    repeat split.
    + unfold max_list. destruct max_dec. now exists (x :: xs).
      destruct Hs1 as [[suf Hsuf] _]. exists suf. now subst.
    + intros [|xb b] [suf Hsuf]; rewrite total_max_list; [apply le_max_l|].
      inversion Hsuf. subst. cbn.
      transitivity (xb + total s1); [|apply le_max_r].
      destruct Hs1 as [_ Hmax]; apply add_le_mono_l, Hmax.
      now exists suf.
    + destruct Hs1 as [[suf1 Hsuf1] _], Hs2 as [[pre2 [suf2 Hsub2]] _].
      unfold max_list. destruct max_dec; [exists [], suf1; now rewrite Hsuf1|].
      exists (x :: pre2), suf2; now rewrite Hsub2.
    + intros b [[|xb pre] [suf Hb]]; rewrite total_max_list.
      * destruct Hs1 as [_ Hmax1], Hs2 as [_ Hmax2].
        destruct b as [|xb b]; [transitivity (total s2); [apply Hmax2; now exists nil, xs|apply le_max_r]|].
        inversion Hb. subst. cbn.
        transitivity (xb + total s1); [|apply le_max_l].
        apply add_le_mono_l, Hmax1; now exists suf.
      * transitivity (total s2); [|apply le_max_r].
        inversion Hb. subst.
        destruct Hs2 as [_ Hmax]; apply Hmax.
        now exists pre, suf.
    + unfold max_list. cbn.
      destruct max_dec as [Hmax1|Hmax1], max_dec as [Hmax2|Hmax2]; now rewrite Hmax1, Hmax2.
Qed.

Theorem max_sub_sum_correct : forall (lst : list Z),
  exists s, Max_sub_sum s lst /\ total s = max_sub_sum lst.
Proof.
  intros. destruct (max_sub_sum_aux_correct lst) as [s1 [s2 [Hpre [Hsub Hmax]]]].
  exists s2. split; [easy|].
  unfold max_sub_sum. now rewrite <- Hmax.
Qed.
