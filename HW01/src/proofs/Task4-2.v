Theorem interchg_or: forall a b : Prop,
   (a \/ b) <-> (~a -> b).
Proof.
   intros. split. intros. apply NNPP. intro. elim H.
   intro. contradiction. intro. contradiction. intro.
   apply NNPP. intro. elim H0. right. apply NNPP. intro.
   apply H1. apply H. intro. apply H0. left. assumption.
Qed.

Theorem distrib_or: forall a b c : Prop,
   (a -> b \/ c) <-> (a -> b) \/ (a -> c).
Proof.
   intros. split. 2 : {
     intros. elim H. intro. left. apply (H1 H0).
     intro. right. apply (H1 H0).
   }
   intros. rewrite (interchg_or (a -> b) (a -> c)).
   intros. elim H. intro. elim H0. refine (fun H1 => H2).
   apply id. assumption.
Qed.

Theorem big_o_conseq : forall f g : nat -> nat,
   ConditionBig BigO f g <-> (ConditionSmall SmallO f g \/ ConditionTheta BigTheta f g).
Proof.
   split. rewrite distrib_or.
   right.
   unfold ConditionBig, ConditionTheta, BigO, BigTheta.
   intros.

   destruct H as [c F].
   exists c. exists c.
   intros. destruct H.
   destruct F as [N G]. assumption.
   exists N. intros.
   pose proof (G n H1) as G.
   split.
   2 : { assumption. }
Abort.
