Definition g := (fun n => 9 * n).
Definition f := (fun n => n * n * n).
Definition sum := (fun n => f(n) + g(n)).

Theorem small_o_conseq :
  ConditionSmall SmallO g f -> ConditionTheta BigTheta sum f.
Proof.
  unfold ConditionSmall, SmallO, ConditionTheta, BigTheta.
  unfold sum, f, g.
  intros.
  exists 1. intros.
  exists 3. intros.
  exists 3. intros.
  split.
  - rewrite Nat.mul_1_l.
    rewrite (Nat.mul_comm 9 n).
    rewrite <- (Nat.mul_comm n (n * n)).
    rewrite <- (Nat.mul_add_distr_l n (n * n) 9).
    rewrite <- Nat.mul_le_mono_pos_l. lia. lia.
  - repeat rewrite Nat.mul_assoc.
    rewrite (Nat.mul_comm 9 n).
    rewrite <- (Nat.mul_comm n (n * n)).
    rewrite <- (Nat.mul_add_distr_l n (n * n) 9).
    rewrite (Nat.mul_comm 3 n).
    rewrite (Nat.mul_comm (n * 3) n).
    rewrite <- (Nat.mul_assoc n (n * 3) n).
    rewrite <- Nat.mul_le_mono_pos_l. lia. lia.
Qed.
