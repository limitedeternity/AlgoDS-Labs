Theorem Task3 : forall f g : nat -> nat,
    ConditionTheta
    (fun c1 c2 n f g =>
      BigTheta c1 c2 n f g /\ BigTheta c1 c2 n g f -> BigO c2 n f g \/ BigO c1 n g f
    ) f g.
Proof.
   intros.
   unfold ConditionTheta, BigTheta, BigO.
   exists 1. exists 3. intros.
   exists 0. intros. left.
   destruct H1 as [G F].
   destruct G as [G1 G2].
   assumption.
Qed.
