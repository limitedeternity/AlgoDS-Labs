Theorem Task1 : forall f g : nat -> nat,
   ConditionTheta (
      ThetaRelation eq
      BigTheta
      (fun c1 c2 n f g => BigOmega c1 n f g /\ BigO c2 n f g)
   ) f g.
Proof.
   unfold ConditionTheta, ThetaRelation, BigTheta, BigO, BigOmega.
   intros.
   exists 3. exists 4. intros.
   exists 0. intros.
   reflexivity.
Qed.
