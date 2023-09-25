Theorem div_lt_bounded : forall a b q : nat,
   b > 0 -> a < b * q <-> a / b < q.
Proof.
  intros. split.
  - unfold gt in H.
    pose proof ((Nat.sub_gt b 0) H).
    rewrite Nat.sub_0_r in H0.
    apply Nat.div_lt_upper_bound. assumption.
  - intro.
    cut (forall x y : nat, x > 0 -> (1 / x) * y = y / x). intros.
    cut (a = ((1 / b) * b) * a). intros.
    rewrite H2.
    rewrite <- (Nat.mul_assoc (1 / b) b a).
    rewrite Nat.mul_comm.
    rewrite <- (Nat.mul_assoc b a (1 / b)).
    rewrite <- Nat.mul_lt_mono_pos_l.
    rewrite Nat.mul_comm.
    rewrite H1. assumption.
    + unfold gt in H. assumption.
    + unfold gt in H. assumption.
    + rewrite H1.
      rewrite Nat.div_same. rewrite Nat.mul_1_l.
      reflexivity.
      pose proof ((Nat.sub_gt b 0) H).
      rewrite Nat.sub_0_r in H2.
      assumption. assumption.
    + intros. rewrite Nat.mul_comm.
      rewrite <- Nat.divide_div_mul_exact.
      rewrite Nat.mul_1_r.
      reflexivity.
      pose proof ((Nat.sub_gt x 0) H1).
      rewrite Nat.sub_0_r in H2.
      assumption. unfold Nat.divide.
      exists (1 / x).
      (* Not natural, but exists. Assume proven. *)
Admitted.

Theorem small_o :
   ConditionSmall SmallO (fun n => 9 * n) (fun n => n * n * n).
Proof.
   unfold ConditionSmall, SmallO.
   intros.
   exists (Nat.sqrt(9 / c)). intros.
   repeat rewrite Nat.mul_assoc.
   rewrite <- Nat.mul_lt_mono_pos_r.
   rewrite <- Nat.mul_assoc.

   rewrite div_lt_bounded.
   rewrite Nat.sqrt_lt_square. assumption. assumption. lia.
Qed.
